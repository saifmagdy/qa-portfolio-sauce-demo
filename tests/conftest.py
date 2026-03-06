"""
conftest.py - Pytest Configuration and Fixtures
QA Portfolio: Sauce Demo E-Commerce Application
Author: Saif Magdy
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


BASE_URL = "https://www.saucedemo.com"
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False)
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope="session")
def browser_name(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="function")
def driver(request):
    headless = request.config.getoption("--headless")
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def logged_in_driver(driver):
    driver.get(BASE_URL)
    driver.find_element("id", "user-name").send_keys(VALID_USERNAME)
    driver.find_element("id", "password").send_keys(VALID_PASSWORD)
    driver.find_element("id", "login-button").click()
    assert "/inventory.html" in driver.current_url
    yield driver


@pytest.fixture(scope="function")
def cart_with_items(logged_in_driver):
    driver = logged_in_driver
    add_buttons = driver.find_elements("css selector", "[data-test^='add-to-cart']")
    add_buttons[0].click()
    add_buttons[1].click()
    yield driver
