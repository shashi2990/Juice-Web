# pages/home_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    def close_welcome_banner(self):
        self.click_element(By.XPATH, "//button[@aria-label='Close Welcome Banner']")

    def dismiss_cookie_banner(self):
        self.click_element(By.XPATH, "//a[@class='cc-btn cc-dismiss']")

    def scroll_and_paginate(self):
        self.scroll_to_bottom()
        self.scroll_to_bottom()
        self.scroll_to_bottom()
        self.click_element(By.XPATH, "//div[@class='mat-select-arrow-wrapper ng-tns-c30-10']")
        self.click_element(By.XPATH, "(//span[@class='mat-option-text'])[4]")
