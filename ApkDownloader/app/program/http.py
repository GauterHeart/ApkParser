import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from app.controller.v1.http import HttpControllerV1
from app.core.initer import IniterService
from app.pkg.arch import AppABC
from app.pkg.database import Redis
from app.pkg.exception.base import BaseExceptionHandler
from app.program.app import BaseApp


class HttpApp(BaseApp, AppABC):
    name = "http"

    __app = FastAPI()

    def __init__(self) -> None:
        self.__redis_connection()
        self.__reg_controller()
        self.__reg_middleware()

    def __redis_connection(self) -> None:
        IniterService.cursor_r = Redis(
            host=self._config.REDIS_HOST,
            port=self._config.REDIS_PORT,
            user=self._config.REDIS_USER,
            password=self._config.REDIS_PASSWORD,
            db=self._config.REDIS_DB,
        )
        IniterService.health_connection_redis()

    def __init_controller_v1(self) -> HttpControllerV1:
        return HttpControllerV1(
            file_handler=self._file_handler, auth_service=self._auth_service
        )

    @staticmethod
    @__app.exception_handler(BaseExceptionHandler)
    async def validation_exception_handler(
        request: Request, exc: BaseExceptionHandler
    ) -> JSONResponse:
        _ = request
        return JSONResponse(exc.detail, status_code=exc.status_code)

    def __reg_controller(self) -> None:
        self.__app.include_router(router=self.__init_controller_v1().router)

    def __reg_middleware(self) -> None:
        self.__app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def run(self) -> None:
        uvicorn.run(
            self.__app,
            host=self._config.HOST,
            port=self._config.PORT,
            workers=self._config.WORKER,
        )
