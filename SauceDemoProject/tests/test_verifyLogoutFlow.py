import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


def logout(driver):
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
    burger_menu = driver.find_element(By.CSS_SELECTOR, ".bm-burger-button")
    burger_menu.click()
    logout_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#logout_sidebar_link")))
    logout_link.click()
    return driver.current_url


@pytest.mark.critical
def test_logout_successfully(login, driver):
    actual_url = logout(driver)
    expected_url = "https://www.saucedemo.com/"
    assert actual_url == expected_url, "User was not able to logout successfully"
