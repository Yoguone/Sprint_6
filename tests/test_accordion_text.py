import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        accordion_panel = driver.find_element(*MainPageLocators.accordion)
        driver.execute_script("arguments[0].scrollIntoView();",accordion_panel)
        button = driver.find_element(By.XPATH, f"//div[@role='button' and contains(text(), '{button_text}')]")
        button.click()
        accordion_panel_buttons = WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.XPATH, f"//div[@data-accordion-component='AccordionItemPanel' and not(@hidden)]")))
        WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.XPATH, f"//div[@role='button' and contains(text(), '{button_text}')]")))
        actual_text = accordion_panel_buttons.find_element(By.TAG_NAME, "p").text
        assert actual_text == expected_text