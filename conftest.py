import pytest

from selenium import webdriver
from config import URL

@pytest.fixture()
def driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.get(URL)
    yield
    driver.quit()
