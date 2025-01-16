# driver/driver_factory.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from config.config import IMPLICIT_WAIT, PAGE_LOAD_TIMEOUT


class DriverFactory:

    @staticmethod
    def get_driver(browser="chrome"):
        if browser == "chrome":
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        elif browser == "firefox":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        else:
            raise ValueError("Browser not supported.")

        driver.implicitly_wait(IMPLICIT_WAIT)
        driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
        driver.maximize_window()
        return driver
