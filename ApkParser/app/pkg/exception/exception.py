from .base import BaseExceptionHandler


class UnauthorizedException(BaseExceptionHandler):
    status_code = 401
    detail = "Invalid password or login"


class IdAlreadyExistException(BaseExceptionHandler):
    status_code = 401
    detail = "Id already exist"


class UnixtimeExpiredException(BaseExceptionHandler):
    status_code = 401
    detail = "Unixtime expired"


class InvalidCredentialException(BaseExceptionHandler):
    status_code = 401
    detail = "Invalid credential"
