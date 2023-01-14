from fastapi import APIRouter, Depends

from app.controller.v1.handler import FileHandler
from app.core.auth import AuthService
from app.pkg.arch import HttpControllerABC

from .file import FileHttpController


class HttpControllerV1(HttpControllerABC):
    router = APIRouter(prefix="/v1")

    def __init__(self, file_handler: FileHandler, auth_service: AuthService) -> None:
        self.__file_handler = file_handler
        self.__auth_service = auth_service
        self._init_router()

    def _init_router(self) -> None:
        self.router.include_router(
            router=FileHttpController(handler=self.__file_handler).router,
            dependencies=[
                Depends(self.__auth_service.validate_access),
                Depends(self.__auth_service.validate_id),
            ],
        )
