import pytest
from selenium import webdriver
from urls import Url


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(Url.main_page)
    yield driver
    driver.quit()