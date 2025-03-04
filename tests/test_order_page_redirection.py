import allure
from urls import Url
from pages.main_page import MainPage
from locators.MainPageLocators import MainPageLocators
from selenium import webdriver

class TestOrderPageRedirection:
    @allure.title('Проверка работы маленькой кнопки "Заказать"')
    def test_small_order_button_click(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.small_order_button_click()
        expected_url = Url.order_page
        assert driver.current_url == expected_url

    @allure.title('Проверка большой кнопки "Заказать"')
    def test_big_order_button_click(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.big_order_button_click()
        expected_url = Url.order_page
        assert driver.current_url == expected_url