from typing import Any

from fastapi import HTTPException


class BaseExceptionHandler(HTTPException):
    status_code: Any = ...
    detail: Any = ...

    def __init__(self) -> None:
        super().__init__(status_code=self.status_code, detail=self.detail)
