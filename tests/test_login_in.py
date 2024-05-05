import pytest
from conftest import driver
from selenium.webdriver.common.by import By

from tests.locators import *


class TestLoginIn:
    def test_login_in_account(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(By.XPATH, login_in_button).click()
        self.driver.find_element(By.XPATH, email_input).send_keys("123sd@ya.ru")
        self.driver.find_element(By.XPATH, password_input).send_keys(123456)
        self.driver.find_element(By.XPATH, auto_button).click()
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_login_lk(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(By.XPATH, account_button).click()
        self.driver.find_element(By.XPATH, email_input).send_keys("123sd@ya.ru")
        self.driver.find_element(By.XPATH, password_input).send_keys(123456)
        self.driver.find_element(By.XPATH, auto_button).click()
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_login_form_registration(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        self.driver.find_element(By.XPATH, login_link).click()
        self.driver.find_element(By.XPATH, email_input).send_keys("123sd@ya.ru")
        self.driver.find_element(By.XPATH, password_input).send_keys(123456)
        self.driver.find_element(By.XPATH, auto_button).click()
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_login_password_recovery(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")
        self.driver.find_element(By.XPATH, forgot_password_link).click()
        self.driver.find_element(By.XPATH, email_input).send_keys("123sd@ya.ru")
        self.driver.find_element(By.XPATH, password_recovery_button).click()
        self.driver.find_element(By.XPATH, login_link).click()
        self.driver.find_element(By.XPATH, email_input).send_keys("123sd@ya.ru")
        self.driver.find_element(By.XPATH, password_input).send_keys(123456)
        self.driver.find_element(By.XPATH, auto_button).click()
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/"
