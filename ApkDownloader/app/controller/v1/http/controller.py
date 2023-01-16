from fastapi import APIRouter, Depends

from app.controller.v1.handler import InfoHandler
from app.core.auth import AuthService
from app.pkg.arch import HttpControllerABC

from .info import InfoHttpController


class HttpControllerV1(HttpControllerABC):
    router = APIRouter(prefix="/v1")

    def __init__(self, info_handler: InfoHandler, auth_service: AuthService) -> None:
        self.__info_handler = info_handler
        self.__auth_service = auth_service
        self._init_router()

    def _init_router(self) -> None:
        self.router.include_router(
            router=InfoHttpController(handler=self.__info_handler).router,
            dependencies=[
                Depends(self.__auth_service.validate_access),
                Depends(self.__auth_service.validate_id),
            ],
        )
