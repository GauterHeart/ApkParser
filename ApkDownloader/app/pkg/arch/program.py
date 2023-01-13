from abc import ABC, abstractmethod


class AppABC(ABC):
    @abstractmethod
    def run(self) -> None:
        ...

    @property
    @abstractmethod
    def name(self) -> str:
        ...
