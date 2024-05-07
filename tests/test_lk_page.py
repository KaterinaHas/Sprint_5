import pytest

from conftest import driver
from locators import Locators
from data import *
from config import URL


class TestLKPage:
    def test_open_lk(self):
        self.driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*Locators.AUTO_BUTTON).click()
        self.driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        assert self.driver.current_url == f"{URL}/account/profile"

    def test_exit_from_lk(self):
        self.driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*Locators.AUTO_BUTTON).click()
        self.driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        self.driver.find_element(*Locators.LOG_OUT_BUTTON).click()
        assert self.driver.current_url == f"{URL}/login"
