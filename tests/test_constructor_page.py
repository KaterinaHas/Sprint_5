import pytest
from conftest import driver

from tests.locators import Locators


class TestConstructorPage:
    def test_open_constructor(self):
        self.driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        self.driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_open_sauces_section(self):
        self.driver.find_element(*Locators.SAUCES_ITEM).click()
        select_section = self.driver.find_element(*Locators.SAUCES_ITEM).get_attribute("class")
        not_select_section_bun = self.driver.find_element(*Locators.BUN_ITEM).get_attribute("class")
        not_select_section_filling = self.driver.find_element(*Locators.FILLING_ITEM).get_attribute("class")
        assert "type_current" in select_section
        assert "type_current" not in not_select_section_bun
        assert "type_current" not in not_select_section_filling

    def test_open_bun_section(self):
        self.driver.find_element(*Locators.BUN_ITEM).click()
        select_section = self.driver.find_element(*Locators.BUN_ITEM).get_attribute("class")
        not_select_section_sauces = self.driver.find_element(*Locators.SAUCES_ITEM).get_attribute("class")
        not_select_section_filling = self.driver.find_element(*Locators.FILLING_ITEM).get_attribute("class")
        assert "type_current" in select_section
        assert "type_current" not in not_select_section_sauces
        assert "type_current" not in not_select_section_filling

    def test_open_filling_section(self):
        self.driver.find_element(*Locators.FILLING_ITEM).click()
        select_section = self.driver.find_element(*Locators.FILLING_ITEM).get_attribute("class")
        not_select_section_bun = self.driver.find_element(*Locators.BUN_ITEM).get_attribute("class")
        not_select_section_sauces = self.driver.find_element(*Locators.SAUCES_ITEM).get_attribute("class")
        assert "type_current" in select_section
        assert "type_current" not in not_select_section_bun
        assert "type_current" not in not_select_section_sauces
