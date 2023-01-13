from .base import BaseRabbitException


class RabbitModelValidatorException(BaseRabbitException):
    status_code = 422
    detail = "Model is not valid"
