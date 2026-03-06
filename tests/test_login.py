"""
test_login.py - Login / Authentication Test Suite
QA Portfolio: Sauce Demo E-Commerce Application
Author: Saif Magdy
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com"


class TestLogin:

    def _navigate_to_login(self, driver):
        driver.get(BASE_URL)

    def _enter_credentials(self, driver, username, password):
        driver.find_element(By.ID, "user-name").clear()
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys(password)

    def _click_login(self, driver):
        driver.find_element(By.ID, "login-button").click()

    def _get_error_message(self, driver):
        wait = WebDriverWait(driver, 5)
        error_elem = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )
        return error_elem.text

    def test_valid_login_redirects_to_inventory(self, driver):
        self._navigate_to_login(driver)
        self._enter_credentials(driver, "standard_user", "secret_sauce")
        self._click_login(driver)
        assert "/inventory.html" in driver.current_url
        page_title = driver.find_element(By.CLASS_NAME, "title").text
        assert page_title == "Products"

    def test_invalid_password_shows_error(self, driver):
        self._navigate_to_login(driver)
        self._enter_credentials(driver, "standard_user", "wrongpassword")
        self._click_login(driver)
        assert "/inventory" not in driver.current_url
        error_text = self._get_error_message(driver)
        assert "Username and password do not match" in error_text

    def test_empty_credentials_shows_username_required_error(self, driver):
        self._navigate_to_login(driver)
        self._click_login(driver)
        error_text = self._get_error_message(driver)
        assert "Username is required" in error_text

    def test_locked_out_user_cannot_login(self, driver):
        self._navigate_to_login(driver)
        self._enter_credentials(driver, "locked_out_user", "secret_sauce")
        self._click_login(driver)
        assert "/inventory" not in driver.current_url
        error_text = self._get_error_message(driver)
        assert "locked out" in error_text.lower()

    def test_logout_redirects_to_login_page(self, driver):
        self._navigate_to_login(driver)
        self._enter_credentials(driver, "standard_user", "secret_sauce")
        self._click_login(driver)
        assert "/inventory.html" in driver.current_url
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        wait = WebDriverWait(driver, 5)
        logout_link = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout_link.click()
        assert driver.find_element(By.ID, "login-button").is_displayed()

    def test_missing_username_only_shows_error(self, driver):
        self._navigate_to_login(driver)
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self._click_login(driver)
        error_text = self._get_error_message(driver)
        assert "Username is required" in error_text
