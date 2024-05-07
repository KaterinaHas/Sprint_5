import pytest

from config import URL
from conftest import driver
from selenium.webdriver.common.by import By
from data import *
from tests.locators import Locators


class TestRegistrationPage:
    def test_correct_registration(self):
        email, password = get_sign_up_data()
        self.driver.find_element(*Locators.LOGIN_IN_BUTTON).click()
        self.driver.find_element(*Locators.REGISTRATION_LINK).click()
        self.driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        assert self.driver.current_url == f"{URL}/login"

    def test_not_correct_password_in_registration(self):
        self.driver.find_element(*Locators.LOGIN_IN_BUTTON).click()
        self.driver.find_element(*Locators.REGISTRATION_LINK).click()
        self.driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(12345)
        self.driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        assert self.driver.find_element(*Locators.NOT_CORRECT_PASSWORD_ERROR).text == "Некорректный пароль"
