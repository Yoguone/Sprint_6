import allure

from pages.base_page import BasePage
from urls import Url
from locators.MainPageLocators import MainPageLocators
from locators.OrderPageLocators import OrderPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = MainPageLocators

    @allure.step('Открыть главную страницу')
    def open_main_page(self):
        self.page_open(Url.main_page)

    @allure.step('Нажать на маленькую кнопку "Заказать"')
    def small_order_button_click(self):
        self.element_click(self.locator.small_order_button)

    @allure.step('Нажать на большую кнопку "Заказать"')
    def big_order_button_click(self):
        big_order_button = self.find_page_element(self.locator.big_order_button)
        self.scroll_to_element(big_order_button)
        self.wait_for_visible(self.locator.big_order_button)
        self.element_click(self.locator.big_order_button)

    @allure.step('Нажать на логотип "Скутер"')
    def scooter_logo_click(self):
        self.element_click(OrderPageLocators.scooter_logo)

    @allure.step('Нажать на логотип "Яндекс"')
    def yandex_logo_click(self):
        self.element_click(MainPageLocators.yandex_logo)
        self.wait_for_new_window(2)
        self.switch_window(1)
        self.wait_for_url_changed(Url.dzen_page)

    @allure.step('Нажать на кнопку в выпадающем списке')
    def accordion_button_click(self, button_text):
        self.element_click(self.locator.accordion_button(button_text))


