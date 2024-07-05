import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest_html
from pytest_metadata.plugin import metadata_key


@pytest.fixture(scope="class")
def driver():
    """
    Fixture to set up and tear down the WebDriver instance.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def login(driver):
    """
    Fixture to perform login operation.
    """
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    yield


def pytest_html_report_title(report):
    report.title = "Pytest HTML Report on SauceDemo"


def pytest_configure(config):
    config.stash[metadata_key]["Project"] = "Test Automation for www.saucedemo.com"
