from selenium import webdriver
from selenium.webdriver.firefox.options import Options


url = 'https://www.apkmirror.com/apk/k-health/k-health-telehealth-primary-care-pediatrics/k-health-telehealth-primary-care-pediatrics-4-105-1-release/k-health-24-7-virtual-care-4-105-1-android-apk-download/download/?key=af036864352830b1e08bead23d614df1f58f1442&forcebaseapk=true'

options = Options()
options.add_argument("--headless")
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir", './')

# options.add_argument("download.default_directory=./")
driver = webdriver.Firefox(options=options)
driver.get(url)
