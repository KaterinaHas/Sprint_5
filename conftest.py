import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield
    driver.quit()
