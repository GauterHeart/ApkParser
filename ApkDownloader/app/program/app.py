from app.config.config import get_settings
from app.controller.v1.handler import DownloadHandler
from app.core.downloader import SeleniumDownloader
from app.core.rabbit.status import RabbitStatusHandler


class BaseApp:
    _config = get_settings()

    _selenium_downloader = SeleniumDownloader(path=_config.DOWNLOADER_PATH)

    _download_handler = DownloadHandler()
    _rabbit_status_handler = RabbitStatusHandler()
