import hashlib
import hmac
from time import time

from cryptography.fernet import Fernet
from fastapi import Header, Request

from app.core.namespace import LifeCycleNS
from app.crud import PostgresCRUD, RedisCRUD
from app.pkg.exception import (
    IdAlreadyExistException,
    InvalidCredentialException,
    UnixtimeExpiredException,
)


class AuthService:
    def __init__(
        self,
        crud_p: PostgresCRUD,
        crud_r: RedisCRUD,
        fernet: Fernet,
    ) -> None:
        self.__crud_p = crud_p
        self.__crud_r = crud_r
        self.__fernet = fernet

    def __decode_private(self, private_key: bytes) -> bytes:
        return self.__fernet.decrypt(private_key)

    def __make_signature(self, data: bytes, private_key: str) -> str:
        return hmac.new(
            self.__decode_private(private_key=private_key.encode("utf-8")),
            data,
            hashlib.sha512,
        ).hexdigest()

    async def validate_access(
        self,
        req: Request,
        signature: str = Header(...),
        public_key: str = Header(...),
    ) -> None:

        effect = await self.__crud_p.client.get(public_key=public_key)
        if effect is None:
            raise InvalidCredentialException()

        data = await req.body()
        new_signature = self.__make_signature(data=data, private_key=effect.private_key)

        if new_signature != signature:
            raise InvalidCredentialException()

    async def validate_id(self, req: Request, id: str = Header(...)) -> None:

        data = await req.json()
        if "unixtime" not in data:
            raise InvalidCredentialException()

        unixtime = data["unixtime"]
        if int(unixtime) + LifeCycleNS.UNIXTIME.value < int(time()):
            raise UnixtimeExpiredException()

        effect = await self.__crud_r.auth.get(request_id=id)
        if effect is not None:
            raise IdAlreadyExistException()

        await self.__crud_r.auth.create(
            request_id=id,
            unixtime=unixtime,
            expire=LifeCycleNS.REQUEST_ID.value,
        )
