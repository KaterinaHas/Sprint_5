import pytest
from conftest import driver
from selenium.webdriver.common.by import By

from locators import *


class TestConstructorPage:
    def test_open_constructor(self):
        self.driver.get("https://stellarburgers.nomoreparties.site")
        self.driver.find_element(By.XPATH, account_button).click()
        self.driver.find_element(By.XPATH, constructor_button).click()
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_open_sauces_section(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(By.XPATH, sauces_item).click()
        select_section = self.driver.find_element(By.XPATH, sauces_item).get_attribute("class")
        not_select_section_bun = self.driver.find_element(By.XPATH, bun_item).get_attribute("class")
        not_select_section_filling = self.driver.find_element(By.XPATH, filling_item).get_attribute("class")
        assert "type_current" in select_section
        assert "type_current" not in not_select_section_bun
        assert "type_current" not in not_select_section_filling

    def test_open_bun_section(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(By.XPATH, bun_item).click()
        select_section = self.driver.find_element(By.XPATH, bun_item).get_attribute("class")
        not_select_section_sauces = self.driver.find_element(By.XPATH, sauces_item).get_attribute("class")
        not_select_section_filling = self.driver.find_element(By.XPATH, filling_item).get_attribute("class")
        assert "type_current" in select_section
        assert "type_current" not in not_select_section_sauces
        assert "type_current" not in not_select_section_filling

    def test_open_filling_section(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(By.XPATH, filling_item).click()
        select_section = self.driver.find_element(By.XPATH, filling_item).get_attribute("class")
        not_select_section_bun = self.driver.find_element(By.XPATH, bun_item).get_attribute("class")
        not_select_section_sauces = self.driver.find_element(By.XPATH, sauces_item).get_attribute("class")
        assert "type_current" in select_section
        assert "type_current" not in not_select_section_bun
        assert "type_current" not in not_select_section_sauces
