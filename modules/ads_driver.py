from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


class AdsDriver:
    def __init__(self, ads_info):
        self.driver = self._initiate_driver(ads_info)

    @classmethod
    def _initiate_driver(cls, ads_info):
        print(ads_info)
        chrome_driver_path = ads_info["data"]["webdriver"]
        debugger_address = ads_info["data"]["ws"]["selenium"]
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", debugger_address)
        service = Service(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver

    def close_driver(self):
        self.driver.quit()
