import pytest
from conftest import driver

from locators import Locators


class TestLKPage:
    def test_open_lk(self):
        self.driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys("123sd@ya.ru")
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(123456)
        self.driver.find_element(*Locators.AUTO_BUTTON).click()
        self.driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

    def test_exit_from_lk(self):
        self.driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys("123sd@ya.ru")
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(123456)
        self.driver.find_element(*Locators.AUTO_BUTTON).click()
        self.driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        self.driver.find_element(*Locators.LOG_OUT_BUTTON).click()
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/login"
