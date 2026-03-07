"""
test_products.py - Product Catalog Test Suite
QA Portfolio: Sauce Demo E-Commerce Application
Author: Saif Magdy
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com"


class TestProductCatalog:

    def _get_product_names(self, driver):
        items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [item.text for item in items]

    def _get_product_prices(self, driver):
        prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        return [float(p.text.replace("$", "")) for p in prices]

    def _sort_products(self, driver, option_value):
        select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
        select.select_by_value(option_value)

    # TC-PC-001
    @pytest.mark.smoke
    def test_products_page_displays_all_items(self, logged_in_driver):
        driver = logged_in_driver
        items = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(items) == 6, f"Expected 6 products, found {len(items)}"

    # TC-PC-002
    @pytest.mark.smoke
    def test_each_product_has_name_price_and_image(self, logged_in_driver):
        driver = logged_in_driver
        items = driver.find_elements(By.CLASS_NAME, "inventory_item")
        for item in items:
            assert item.find_element(By.CLASS_NAME, "inventory_item_name").text != ""
            price_text = item.find_element(By.CLASS_NAME, "inventory_item_price").text
            assert price_text.startswith("$")
            img = item.find_element(By.CLASS_NAME, "inventory_item_img")
            assert img is not None

    # TC-PC-003
    @pytest.mark.regression
    def test_sort_by_name_a_to_z(self, logged_in_driver):
        driver = logged_in_driver
        self._sort_products(driver, "az")
        names = self._get_product_names(driver)
        assert names == sorted(names), "Products are not sorted A-Z"

    # TC-PC-004
    @pytest.mark.regression
    def test_sort_by_price_low_to_high(self, logged_in_driver):
        driver = logged_in_driver
        self._sort_products(driver, "lohi")
        prices = self._get_product_prices(driver)
        assert prices == sorted(prices), "Prices are not sorted low to high"

    # TC-PC-005
    @pytest.mark.regression
    def test_product_detail_page_loads(self, logged_in_driver):
        driver = logged_in_driver
        first_product = driver.find_element(By.CLASS_NAME, "inventory_item_name")
        product_name = first_product.text
        first_product.click()
        wait = WebDriverWait(driver, 5)
        detail_name = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_details_name"))
        )
        assert detail_name.text == product_name
        assert driver.find_element(By.CLASS_NAME, "inventory_details_price").is_displayed()
        assert driver.find_element(By.CLASS_NAME, "inventory_details_desc").is_displayed()

    # TC-PC-006
    @pytest.mark.regression
    def test_back_to_products_from_detail(self, logged_in_driver):
        driver = logged_in_driver
        driver.find_element(By.CLASS_NAME, "inventory_item_name").click()
        wait = WebDriverWait(driver, 5)
        back_btn = wait.until(EC.element_to_be_clickable((By.ID, "back-to-products")))
        back_btn.click()
        assert "/inventory.html" in driver.current_url
        assert len(driver.find_elements(By.CLASS_NAME, "inventory_item")) == 6
