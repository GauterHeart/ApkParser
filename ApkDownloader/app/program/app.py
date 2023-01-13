from app.config.config import get_settings
from app.controller.v1.handler import DownloadHandler
from app.core.rabbit.status import RabbitStatusHandler


class BaseApp:
    _config = get_settings()

    _download_handler = DownloadHandler()
    _rabbit_status_handler = RabbitStatusHandler()
