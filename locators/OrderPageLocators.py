from selenium.webdriver.common.by import By

class OrderPageLocators:
    renter_form_header = By.XPATH, '/html/body/div/div/div[2]/div[1]'
    name_input = By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/input'
    surname_input = By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/input'
    address_input = By.XPATH, '/html/body/div/div/div[2]/div[2]/div[3]/input'
    phone_number_input = By.XPATH, '/html/body/div/div/div[2]/div[2]/div[5]/input'
    further_button = By.XPATH, '/html/body/div/div/div[2]/div[3]/button'
    calendar_input = By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/div[1]/div/input'
    rent_time_arrow = By.XPATH, "//div/span[@class='Dropdown-arrow']"
    rent_time_dropdown_menu_1day = By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div[1]"
    black_scooter_checkbox = By.XPATH, '//*[@id="black"]'
    grey_scooter_checkbox = By.XPATH, '//*[@id="grey"]'
    comment_input = By.XPATH, '/html/body/div/div/div[2]/div[2]/div[4]/input'
    datepicker = By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/div[1]/div/input'
    order_page_order_button = By.XPATH, '/html/body/div/div/div[2]/div[3]/button[2]'
    confirm_window_header = By.XPATH, '/html/body/div/div/div[2]/div[5]/div[1]'
    confirm_button = By.XPATH, '/html/body/div/div/div[2]/div[5]/div[2]/button[2]'
    order_done_modal = By.XPATH, '/html/body/div/div/div[2]/div[5]'
    scooter_logo = By.XPATH, '/html/body/div/div/div[1]/div[1]/a[2]/img'
    pick_metro_station = By.XPATH, '/html/body/div/div/div[2]/div[2]/div[4]/div/div/input'
    metro_station_dropdown_menu = By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[4]/div/div[2]'
    metro_input = By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[4]/div/div/input'
    metro_station = By.XPATH, "//div[@class='select-search__select']//*[contains(text(), 'Черкизовская')]"
