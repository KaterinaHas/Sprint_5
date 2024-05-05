import pytest
from conftest import driver
from selenium.webdriver.common.by import By

from tests.locators import *


class TestRegistrationPage:
    def test_correct_registration(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(By.XPATH, login_in_button).click()
        self.driver.find_element(By.XPATH, registration_link).click()
        self.driver.find_element(By.XPATH, name_input).send_keys("Kiril")
        self.driver.find_element(By.XPATH, email_input).send_keys("123sdd@ya.ru")
        self.driver.find_element(By.XPATH, password_input).send_keys(123456)
        self.driver.find_element(By.XPATH, registration_button).click()
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_not_correct_password_in_registration(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(By.XPATH, login_in_button).click()
        self.driver.find_element(By.XPATH, registration_link).click()
        self.driver.find_element(By.XPATH, name_input).send_keys("Kiril")
        self.driver.find_element(By.XPATH, email_input).send_keys("123@ya.ru")
        self.driver.find_element(By.XPATH, password_input).send_keys(12345)
        self.driver.find_element(By.XPATH, registration_button).click()
        assert self.driver.find_element(By.XPATH, "//p[text()='Некорректный пароль']").text == "Некорректный пароль"
