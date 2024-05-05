import pytest
from conftest import driver

from tests.locators import Locators


class TestLoginIn:
    def test_login_in_account(self):
        self.driver.find_element(*Locators.LOGIN_IN_BUTTON).click()
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys("123sd@ya.ru")
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(123456)
        self.driver.find_element(*Locators.AUTO_BUTTON).click()
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_login_lk(self):
        self.driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys("123sd@ya.ru")
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(123456)
        self.driver.find_element(*Locators.AUTO_BUTTON).click()
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_login_form_registration(self):
        self.driver.find_element(*Locators.LOGIN_IN_BUTTON).click()
        self.driver.find_element(*Locators.REGISTRATION_LINK).click()
        self.driver.find_element(*Locators.LOGIN_LINK).click()
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys("123sd@ya.ru")
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(123456)
        self.driver.find_element(*Locators.AUTO_BUTTON).click()
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_login_password_recovery(self):
        self.driver.find_element(*Locators.LOGIN_IN_BUTTON).click()
        self.driver.find_element(*Locators.FORGOT_PASSWORD_LINK).click()
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys("123sd@ya.ru")
        self.driver.find_element(*Locators.PASSWORD_RECOVERY_BUTTON).click()
        self.driver.find_element(*Locators.LOGIN_LINK).click()
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys("123sd@ya.ru")
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(123456)
        self.driver.find_element(*Locators.AUTO_BUTTON).click()
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/"
