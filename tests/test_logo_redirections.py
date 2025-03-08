import allure
from pages.main_page import MainPage
from urls import Url

class TestLogoRedirections:
    @allure.title('Проверка редиректа на главную страницу "Yandex" при клике на логотип Yandex')
    def test_redirect_from_yandex_logo_successful(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.yandex_logo_click()
        expected_url = Url.dzen_page
        assert driver.current_url == expected_url

    @allure.title('Проверка редиректа на главную страницу при клике на логотип самоката')
    def test_redirect_from_scooter_logo_successful(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.small_order_button_click()
        main_page.scooter_logo_click()
        expected_url = Url.main_page
        assert driver.current_url == expected_url
