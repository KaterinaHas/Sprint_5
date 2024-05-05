import pytest
from conftest import driver
from selenium.webdriver.common.by import By

from tests.locators import *


class TestLKPage:
    def test_open_lk(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(By.XPATH, account_button).click()
        self.driver.find_element(By.XPATH, email_input).send_keys("123sd@ya.ru")
        self.driver.find_element(By.XPATH, password_input).send_keys(123456)
        self.driver.find_element(By.XPATH, auto_button).click()
        self.driver.find_element(By.XPATH, account_button).click()
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

    def test_exit_from_lk(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(By.XPATH, account_button).click()
        self.driver.find_element(By.XPATH, email_input).send_keys("123sd@ya.ru")
        self.driver.find_element(By.XPATH, password_input).send_keys(123456)
        self.driver.find_element(By.XPATH, auto_button).click()
        self.driver.find_element(By.XPATH, log_out_button).click()
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/login"
