from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import requests
from ads_power.ads_profiles import AdsProfiles
from selenium import webdriver
from data.constants import CLOSE_URL_ID
import subprocess


class AdsBrowser:
    browser_value = 0

    def __init__(self, ads_info):
        self.driver = self._initiate_driver(ads_info)

    @classmethod
    def _initiate_driver(cls, ads_info):
        chrome_driver_path = ads_info["data"]["webdriver"]
        debugger_address = ads_info["data"]["ws"]["selenium"]
        chrome_options = Options()
        chrome_options.add_argument(f"--user-data-dir=./ads_power/{cls.browser_value}")
        chrome_options.add_experimental_option("debuggerAddress", debugger_address)
        service = Service(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        cls.browser_value += 1
        return driver

    def close_driver(self):
        self.driver.quit()
        requests.get(CLOSE_URL_ID + AdsProfiles.user_ids[0])
        try:
            subprocess.run(['taskkill', '/F', '/IM', 'SunBrowser.exe'], check=True)
        except Exception as e:
            print("Process is not running : " + str(e))

