# pages/base_page.py


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import IMPLICIT_WAIT


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, IMPLICIT_WAIT)

    def click_element(self, by, value):
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()

    def send_keys(self, by, value, text):
        element = self.wait.until(EC.presence_of_element_located((by, value)))
        element.send_keys(text)

    def get_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
