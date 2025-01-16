# pages/register_page.py

import random
import string
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):

    def generate_random_email(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=12)) + "@test.com"

    def generate_random_password(self):
        return ''.join(
            random.choices(string.ascii_letters + string.punctuation + string.ascii_uppercase + string.digits, k=19))

    def generate_random_security_answer(self):
        return ''.join(random.choices(string.ascii_letters + string.ascii_uppercase, k=12))

    def fill_registration_form(self):
        email = self.generate_random_email()
        password = self.generate_random_password()
        answer = self.generate_random_security_answer()

        self.send_keys(By.XPATH, "//div/input[@aria-label='Email address field']", email)
        self.send_keys(By.XPATH, "//div/input[@aria-label='Field for the password']", password)
        self.send_keys(By.XPATH, "//div/input[@aria-label='Field to confirm the password']", password)
        self.send_keys(By.XPATH, "//div/input[@aria-label='Field for the answer to the security question']", answer)

        return email, password
