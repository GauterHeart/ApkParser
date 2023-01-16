from app.pkg.rabbit.exception import BaseRabbitException


class RabbitDownloadException(BaseRabbitException):
    status_code = 500
    detail = "Download Failed"
