# tests/test_juice_shop.py

import time
import pytest
from driver.driver_factory import DriverFactory
from pages.home_page import HomePage
from pages.register_page import RegisterPage


@pytest.fixture(scope="function")
def setup():
    driver = DriverFactory.get_driver()
    driver.get("https://juice-shop.herokuapp.com/")
    yield driver
    driver.quit()


def test_register_new_user(setup):
    driver = setup
    home_page = HomePage(driver)
    register_page = RegisterPage(driver)

    # Close welcome banner and cookie banner
    home_page.close_welcome_banner()
    time.sleep(5)
    home_page.dismiss_cookie_banner()

    # Register a new user
    email, password = register_page.fill_registration_form()
    time.sleep(5)

    # Verify registration success (this can be done by checking for success message, or UI state change)
    assert "Registration successful" in driver.page_source


def test_product_purchase(setup):
    driver = setup
    home_page = HomePage(driver)

    # Scroll and paginate
    home_page.scroll_and_paginate()
    time.sleep(3)
    # Additional test steps for product purchase
    # assert some condition after purchasing
