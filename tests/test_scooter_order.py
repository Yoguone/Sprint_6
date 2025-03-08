import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.OrderPageLocators import OrderPageLocators
from data import Users, Metro, Comments


@allure.title('Заказ самоката через маленькую кнопку "Заказать"')
class TestScooterOrder:
    def test_small_order_button_scooter_rent_successful(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        order_page.main_page_open()
        main_page.small_order_button_click()
        order_page.wait_for_visible(OrderPageLocators.renter_form_header)
        order_page.fill_renter_form(Users.first_user_name, Users.first_user_surname,
                                    Users.first_user_address, Users.first_user_phone)
        metro_input = main_page.find_page_element(OrderPageLocators.metro_input)
        metro_input.send_keys(Metro.metro_station_name)
        metro_station = order_page.wait_for_visible(OrderPageLocators.metro_station)
        metro_station.click()
        order_page.element_click(OrderPageLocators.further_button)
        order_page.fill_rent_details(Comments.comment)
        order_page.confirm_order()
        confirmed_order = main_page.find_page_element(OrderPageLocators.order_done_modal)
        assert confirmed_order.is_displayed()

    @allure.title('Заказ самоката через большую кнопку "Заказать"')
    def test_big_order_button_scooter_rent_successful(self,driver):
         order_page = OrderPage(driver)
         main_page = MainPage(driver)
         order_page.main_page_open()
         main_page.big_order_button_click()
         order_page.wait_for_visible(OrderPageLocators.renter_form_header)
         order_page.fill_renter_form(Users.second_user_name, Users.second_user_surname,
                                     Users.second_user_address, Users.second_user_phone)
         metro_input = main_page.find_page_element(OrderPageLocators.metro_input)
         metro_input.send_keys(Metro.metro_station_name)
         metro_station = order_page.wait_for_visible(OrderPageLocators.metro_station)
         metro_station.click()
         order_page.element_click(OrderPageLocators.further_button)
         order_page.fill_rent_details(Comments.comment)
         order_page.confirm_order()
         confirmed_order = main_page.find_page_element(OrderPageLocators.order_done_modal)
         assert confirmed_order.is_displayed()