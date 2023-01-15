import hashlib
import hmac
from time import time

from cryptography.fernet import Fernet
from fastapi import Header, Request
from pydantic import parse_obj_as

from app.core.namespace import LifeCycleNS
from app.crud import PostgresCRUD, RedisCRUD
from app.pkg.exception import (
    IdAlreadyExistException,
    InvalidCredentialException,
    UnixtimeExpiredException,
)

from .model import AuthSchema


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

    async def validate_id(self, req: Request) -> None:

        data = await req.json()
        try:
            model = parse_obj_as(AuthSchema, data)
        except Exception:
            raise InvalidCredentialException()

        if int(model.unixtime) + LifeCycleNS.UNIXTIME.value < int(time()):
            raise UnixtimeExpiredException()

        effect = await self.__crud_r.auth.get(request_id=model.id)
        if effect is not None:
            raise IdAlreadyExistException()

        await self.__crud_r.auth.create(
            request_id=model.id,
            unixtime=model.unixtime,
            expire=LifeCycleNS.REQUEST_ID.value,
        )
