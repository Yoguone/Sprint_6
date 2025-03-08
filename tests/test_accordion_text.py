import allure
import pytest
from data import buttons_text
from locators.MainPageLocators import MainPageLocators
from pages.main_page import MainPage
from selenium.webdriver.common.by import By


@pytest.mark.parametrize('button_text, expected_text', buttons_text)
class TestAccordionText:
    @allure.title('Проверка выпадающего списка')
    def test_accordion_text(self, button_text, expected_text, driver):
        main_page=MainPage(driver)
        main_page.open_main_page()
        accordion_panel = main_page.find_page_element(MainPageLocators.accordion)
        main_page.scroll_to_element(accordion_panel)
        main_page.accordion_button_click(button_text)
        accordion_panel_buttons = main_page.find_page_element(MainPageLocators.accordion_buttons_text)
        main_page.find_page_element(MainPageLocators.accordion_button(button_text))
        actual_text = accordion_panel_buttons.find_element(By.TAG_NAME, "p").text
        assert actual_text == expected_text