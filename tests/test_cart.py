"""
test_cart.py - Shopping Cart and Checkout Test Suite
QA Portfolio: Sauce Demo E-Commerce Application
Author: Saif Magdy
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com"


class TestShoppingCart:

    def _get_cart_badge_count(self, driver):
        try:
            badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
            return int(badge.text)
        except Exception:
            return 0

    def _navigate_to_cart(self, driver):
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def _get_cart_items(self, driver):
        return driver.find_elements(By.CLASS_NAME, "cart_item")

    def test_add_single_item_updates_cart_badge(self, logged_in_driver):
        driver = logged_in_driver
        assert self._get_cart_badge_count(driver) == 0
        driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
        assert self._get_cart_badge_count(driver) == 1
        remove_button = driver.find_element(By.CSS_SELECTOR, "[data-test='remove-sauce-labs-backpack']")
        assert remove_button.is_displayed()

    def test_add_multiple_items_updates_badge_count(self, logged_in_driver):
        driver = logged_in_driver
        items = ["add-to-cart-sauce-labs-backpack", "add-to-cart-sauce-labs-bike-light", "add-to-cart-sauce-labs-bolt-t-shirt"]
        for item in items:
            driver.find_element(By.CSS_SELECTOR, f"[data-test='{item}']").click()
        assert self._get_cart_badge_count(driver) == 3
        self._navigate_to_cart(driver)
        assert len(self._get_cart_items(driver)) == 3

    def test_remove_item_from_cart(self, logged_in_driver):
        driver = logged_in_driver
        driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
        assert self._get_cart_badge_count(driver) == 1
        self._navigate_to_cart(driver)
        driver.find_element(By.CSS_SELECTOR, "[data-test='remove-sauce-labs-backpack']").click()
        assert self._get_cart_badge_count(driver) == 0
        assert len(self._get_cart_items(driver)) == 0

    def test_cart_persists_after_navigation(self, logged_in_driver):
        driver = logged_in_driver
        driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
        driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-bike-light']").click()
        assert self._get_cart_badge_count(driver) == 2
        driver.find_element(By.CSS_SELECTOR, "[data-test='item-4-title-link']").click()
        driver.find_element(By.ID, "back-to-products").click()
        assert self._get_cart_badge_count(driver) == 2

    @pytest.mark.xfail(reason="BUG-001: App allows checkout with empty cart")
    def test_empty_cart_checkout_shows_error(self, logged_in_driver):
        driver = logged_in_driver
        self._navigate_to_cart(driver)
        checkout_button = driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']")
        assert not checkout_button.is_enabled(), "BUG-001: Checkout should be disabled for empty cart"

    def test_complete_checkout_flow(self, logged_in_driver):
        driver = logged_in_driver
        driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
        self._navigate_to_cart(driver)
        driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']").click()
        driver.find_element(By.CSS_SELECTOR, "[data-test='firstName']").send_keys("Saif")
        driver.find_element(By.CSS_SELECTOR, "[data-test='lastName']").send_keys("Magdy")
        driver.find_element(By.CSS_SELECTOR, "[data-test='postalCode']").send_keys("12345")
        driver.find_element(By.CSS_SELECTOR, "[data-test='continue']").click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_info")))
        driver.find_element(By.CSS_SELECTOR, "[data-test='finish']").click()
        confirmation = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
        assert "Thank you for your order" in confirmation.text

    def test_checkout_missing_first_name_shows_error(self, logged_in_driver):
        driver = logged_in_driver
        driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
        self._navigate_to_cart(driver)
        driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']").click()
        driver.find_element(By.CSS_SELECTOR, "[data-test='lastName']").send_keys("Magdy")
        driver.find_element(By.CSS_SELECTOR, "[data-test='postalCode']").send_keys("12345")
        driver.find_element(By.CSS_SELECTOR, "[data-test='continue']").click()
        wait = WebDriverWait(driver, 5)
        error_elem = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
        assert "First Name is required" in error_elem.text
