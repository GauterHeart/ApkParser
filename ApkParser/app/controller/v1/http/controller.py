from fastapi import APIRouter, Depends

from app.controller.v1.handler import LinkHandler
from app.core.auth import AuthService
from app.pkg.arch import HttpControllerABC

from .link import LinkHttpController


class HttpControllerV1(HttpControllerABC):
    router = APIRouter(prefix="/v1")

    def __init__(self, link_handler: LinkHandler, auth_service: AuthService) -> None:
        self.__link_handler = link_handler
        self.__auth_service = auth_service
        self._init_router()

    def _init_router(self) -> None:
        self.router.include_router(
            router=LinkHttpController(handler=self.__link_handler).router,
            dependencies=[
                Depends(self.__auth_service.validate_access),
                Depends(self.__auth_service.validate_id),
            ],
        )
