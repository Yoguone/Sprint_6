import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу')
    def page_open(self, url):
        self.driver.get(url)

    @allure.step('Кликнуть по элементу')
    def element_click(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Заполнить поле')
    def input_in_the_field(self,locator,text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Дождаться смены адреса')
    def wait_for_url_changed(self, url):
        WebDriverWait(self.driver, 5).until(EC.url_to_be(url))

    @allure.step('Дождаться отображения элемента')
    def wait_for_visible(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

    @allure.step('Дождаться открытия 2 вкладки в браузере')
    def wait_for_new_window(self, window_number):
        WebDriverWait(self.driver, 5).until(EC.number_of_windows_to_be(window_number))

    @allure.step('Найти элемент на странице')
    def find_page_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator))

    @allure.step('Переключиться на другое окно браузера')
    def switch_window(self, window_index):
        self.driver.switch_to.window(self.driver.window_handles[window_index])

    @allure.step('Перейти к элементу')
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
