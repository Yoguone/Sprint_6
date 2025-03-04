from pages.base_page import BasePage
from urls import Url
from locators.MainPageLocators import MainPageLocators
from locators.OrderPageLocators import OrderPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = MainPageLocators

    def open_main_page(self):
        self.page_open(Url.main_page)

    def small_order_button_click(self):
        self.element_click(self.locator.small_order_button)

    def big_order_button_click(self):
        element = self.driver.find_element(*self.locator.big_order_button)
        self.driver.execute_script("arguments[0].scrollIntoView();",element)
        self.element_click(self.locator.big_order_button)

    def scooter_logo_click(self):
        self.driver.find_element(*OrderPageLocators.scooter_logo).click()

    def yandex_logo_click(self):
        self.driver.find_element(*MainPageLocators.yandex_logo).click()
        WebDriverWait(self.driver, 5).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 5).until(EC.url_to_be(Url.dzen_page))

    def click_on_accordion(self, button_index):
        accordion = self.driver.find_element(*MainPageLocators.accordion)
        accordion[button_index].click()