from abc import ABC, abstractmethod

from fastapi import APIRouter


class HttpControllerABC(ABC):
    @property
    @abstractmethod
    def router(self) -> APIRouter:
        ...

    @abstractmethod
    def _init_router(self) -> None:
        ...
