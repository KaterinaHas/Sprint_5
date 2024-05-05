import pytest
from conftest import driver
from selenium.webdriver.common.by import By

from tests.locators import Locators


class TestRegistrationPage:
    def test_correct_registration(self):
        self.driver.find_element(*Locators.LOGIN_IN_BUTTON).click()
        self.driver.find_element(*Locators.REGISTRATION_LINK).click()
        self.driver.find_element(*Locators.NAME_INPUT).send_keys("Kiril")
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys("123sdd@ya.ru")
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(123456)
        self.driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_not_correct_password_in_registration(self):
        self.driver.find_element(*Locators.LOGIN_IN_BUTTON).click()
        self.driver.find_element(*Locators.REGISTRATION_LINK).click()
        self.driver.find_element(*Locators.NAME_INPUT).send_keys("Kiril")
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys("123@ya.ru")
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(12345)
        self.driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        assert self.driver.find_element(By.XPATH, "//p[text()='Некорректный пароль']").text == "Некорректный пароль"
