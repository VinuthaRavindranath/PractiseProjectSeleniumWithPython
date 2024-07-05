import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

low_to_high = "Price (low to high)"
high_to_low = "Price (high to low)"


def get_products(driver):
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
    product_elements = driver.find_elements(By.CLASS_NAME, "inventory_item")
    products = [(product.find_element(By.CLASS_NAME, "inventory_item_name").
                 text, float(product.find_element(By.CLASS_NAME, "inventory_item_price").text.replace('$', '')))
                for product in product_elements]
    return products


def get_products_price(driver):
    products = get_products(driver)
    prices = [price for _, price in products]
    return prices


def get_products_price_low_to_high(driver):
    products = get_products(driver)
    products.sort(key=lambda x: x[1])
    prices = [price for _, price in products]
    return prices


def get_products_price_high_to_low(driver):
    products = get_products(driver)
    products.sort(key=lambda x: x[1], reverse=True)
    prices = [price for _, price in products]
    return prices


def apply_sort_price_filter(driver, visible_text):
    sorting = driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
    select = Select(sorting)
    select.select_by_visible_text(visible_text)


@pytest.mark.medium
def test_sort_products_low_to_high(login, driver):
    expected_price = get_products_price_low_to_high(driver)
    apply_sort_price_filter(driver, low_to_high)
    actual_prices = get_products_price(driver)
    assert actual_prices == expected_price, "sorting price low to high filter is not working as expected"

@pytest.mark.medium
def test_sort_products_high_to_low(login, driver):
    expected_price = get_products_price_high_to_low(driver)
    apply_sort_price_filter(driver, high_to_low)
    actual_prices = get_products_price(driver)
    assert actual_prices == expected_price, "sorting price high to low filter is not working as expected"

