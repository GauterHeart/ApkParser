import asyncio

from bs4 import BeautifulSoup
from pydantic import HttpUrl

from app.crud import PostgresCRUD
from selenium import webdriver

from .main import Parser

a = 'https://downloadr2.apkmirror.com/wp-content/uploads/2023/01/90/63c04ff30714c/ai.kanghealth_4.105.1-61216_minAPI21(arm64-v8a,armeabi-v7a,x86,x86_64)(nodpi)_apkmirror.com.apk?verify=1673548707-1qSKsEMVOyDS-dQtscK1XVzOf_NDPcdDEja8SV3L2vY'

download_link = 'https://downloadr2.apkmirror.com/wp-content/uploads/2023/01/90/63c04ff30714c/ai.kanghealth_4.105.1-61216_minAPI21(arm64-v8a,armeabi-v7a,x86,x86_64)(nodpi)_apkmirror.com.apk?verify=1673548231--pfSiWvpH0XYlfCLrDVXzbcUAKFYv9iLzymFX2f0JZc'

class TestParser(Parser):
    def __init__(self, crud_p: PostgresCRUD, url: HttpUrl, link_len: int) -> None:
        super().__init__(crud_p=crud_p, url=url, link_len=link_len)

    async def download(self) -> None:
        ...

    def run(self) -> None:
        # asyncio.run(self.__test())
        print('start')
        driver = webdriver.Firefox()
        url = 'https://www.apkmirror.com/apk/k-health/k-health-telehealth-primary-care-pediatrics/k-health-telehealth-primary-care-pediatrics-4-105-1-release/k-health-24-7-virtual-care-4-105-1-android-apk-download/download/?key=af036864352830b1e08bead23d614df1f58f1442&forcebaseapk=true'
        driver.get(url=url)

    async def __test(self) -> None:
        # sample = '/apk/k-health/k-health-telehealth-primary-care-pediatrics/k-health-telehealth-primary-care-pediatrics-4-105-1-release/k-health-24-7-virtual-care-4-105-1-android-apk-download/download/?key=d85bdd30fdabee3d6dd1c0132ff6ea3c8ebc2da0&forcebaseapk=true'
        # effect = await self._make_request(route=sample)
        #
        # print(effect.text)
        await self.download()
