# ApkParser


### Схема работы сервисов
![](/static/service.png)


### Что следует улучшить
1. Proxy
2. Request distributor

![](/static/upgrade_service.png)


### Файлы с логикой

Html parser = ./ApkParser/app/core/parser/main.py(получение ссылок)

Downloader = ./ApkDownloader/app/core/downloader/parse_downloader.py