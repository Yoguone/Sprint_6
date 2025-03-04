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