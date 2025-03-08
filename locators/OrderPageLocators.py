from selenium.webdriver.common.by import By
from random import randint

class OrderPageLocators:
    renter_form_header = By.XPATH, '//div/div[contains(text(), "Для кого самокат")]'
    name_input = By.XPATH, '//div/input[@placeholder = "* Имя"]'
    surname_input = By.XPATH, '//div/input[@placeholder = "* Фамилия"]'
    address_input = By.XPATH, '//div/input[@placeholder = "* Адрес: куда привезти заказ"]'
    phone_number_input = By.XPATH, '//div/input[@placeholder = "* Телефон: на него позвонит курьер"]'
    further_button = By.XPATH, '//div/button[contains(text(), "Далее")]'
    calendar_input = By.XPATH, '//div/input[@placeholder = "* Когда привезти самокат"]'
    rent_time_arrow = By.XPATH, "//div/span[@class='Dropdown-arrow']"
    rent_time_dropdown_menu_1day = By.XPATH, f"(//div[@class = 'Dropdown-option'])[{randint(1,5)}]"
    black_scooter_checkbox = By.XPATH, '//*[@id="black"]'
    grey_scooter_checkbox = By.XPATH, '//*[@id="grey"]'
    comment_input = By.XPATH, '//div/input[@placeholder = "Комментарий для курьера"]'
    order_page_order_button = By.XPATH, '//div[@class = "Order_Buttons__1xGrp"]/button[(text() = "Заказать")]'
    confirm_window_header = By.XPATH, '//div/div[contains(text(), "Хотите оформить заказ?")]'
    confirm_button = By.XPATH, '//div[@class = "Order_Buttons__1xGrp"]//button[(text() = "Да")]'
    order_done_modal = By.XPATH, '//div[contains(text(), "Заказ оформлен")]'
    scooter_logo = By.XPATH, '//div/a/img[@alt = "Scooter"]'
    metro_input = By.XPATH, '//div/input[@placeholder = "* Станция метро"]'
    metro_station = By.XPATH, "//div[@class='select-search__select']//*[contains(text(), 'Черкизовская')]"
