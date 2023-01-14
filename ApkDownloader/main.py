from app import app

if __name__ == "__main__":
    app.run()


# import httpx
#
# url = 'https://download.freebsd.org/ftp/releases/amd64/amd64/ISO-IMAGES/12.0/FreeBSD-12.0-RELEASE-amd64-mini-memstick.img'
#
# with open('FreeBSD-12.0-RELEASE-amd64-mini-memstick.img', 'wb') as f:
#     with httpx.stream('GET', url) as r:
#         for chunk in r.iter_bytes():
#             f.write(chunk)

# import httpx
# from bs4 import BeautifulSoup
#
#
# def _make_request(url: str) -> httpx.Response:
#     with httpx.Client() as client:
#         effect = client.get(url=url)
#         return effect
#
#
# def _download_file(url: str) -> None:
#     with open("test_file.apk", "wb") as f:
#         with httpx.stream("GET", url) as r:
#             for chunk in r.iter_bytes():
#                 f.write(chunk)
#
#
# base_url = "https://www.apkmirror.com"
#
#
# def download(url: str) -> None:
#     effect = _make_request(url=url)
#     soup = BeautifulSoup(effect.text, "lxml")
#     href = soup.find("div", {"class": "f-sm-50"}).find("a")["href"]
#     url = "{}{}".format(base_url, href)
#     effect = _make_request(url=url)
#     if effect.status_code == 302:
#         _download_file(url=effect.headers["location"])
#
#
# url = "https://www.apkmirror.com/apk/apna/apna-job-search-india-vacancy-alert-online-work/apna-job-search-india-vacancy-alert-online-work-2023-01-13-release/apna-job-search-alerts-india-2023-01-13-android-apk-download/download/?key=c49bf2d3e9c9e536ef8f84d6ae2d7db9dbf4c0e0&forcebaseapk=true"
#
# download(url=url)
