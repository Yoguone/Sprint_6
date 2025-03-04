import allure

from locators.OrderPageLocators import OrderPageLocators
from pages.base_page import BasePage
from data import Date
from urls import Url

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators

    @allure.step('Открыть главную страницу')
    def main_page_open(self):
        self.page_open(Url.main_page)


    @allure.step('Заполнить информацию о арендаторе')
    def fill_renter_form(self,name,surname,address,phone):
        self.input_in_the_field(self.locators.name_input, name)
        self.input_in_the_field(self.locators.surname_input, surname)
        self.input_in_the_field(self.locators.address_input, address)
        self.input_in_the_field(self.locators.phone_number_input, phone)

    @allure.step('Заполнить информацию о деталях аренды')
    def fill_rent_details(self, comment):
        self.input_in_the_field(self.locators.datepicker, Date.first_rent_date)
        self.element_click(self.locators.rent_time_arrow)
        self.wait_for_visible(self.locators.rent_time_dropdown_menu_1day)
        self.element_click(self.locators.rent_time_dropdown_menu_1day)
        self.input_in_the_field(self.locators.comment_input, comment)
        self.element_click(self.locators.black_scooter_checkbox)
        self.element_click(self.locators.order_page_order_button)

    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        self.element_click(self.locators.confirm_button)
