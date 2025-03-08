from selenium.webdriver.common.by import By

class MainPageLocators:
    small_order_button = By.XPATH, '//div/button[@class = "Button_Button__ra12g"]'
    big_order_button = By.XPATH, '//div/button/parent::div[@class = "Home_FinishButton__1_cWm"]'
    yandex_logo = By.XPATH, '//div/a/img[@alt = "Yandex"]'
    accordion = By.XPATH, '//div[@class = "accordion"]'
    accordion_buttons_text = By.XPATH, f"//div[@data-accordion-component='AccordionItemPanel' and not(@hidden)]"


    @staticmethod
    def accordion_button(button_text):
        return By.XPATH, f"//div[@role='button' and contains(text(), '{button_text}')]"