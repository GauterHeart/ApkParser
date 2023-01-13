from app.config.config import get_settings
from app.core.rabbit.status import RabbitStatusHandler


class BaseApp:
    _config = get_settings()

    _rabbit_status_handler = RabbitStatusHandler()
