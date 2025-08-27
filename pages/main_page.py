from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage:
    URL = "https://stellarburgers.nomoreparties.site"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def click_constructor(self):
        self.driver.find_element(*MainPageLocators.CONSTRUCTOR).click()

    def click_feed(self):
        self.driver.find_element(*MainPageLocators.FEED).click()

    def click_ingredient(self):
        self.driver.find_element(*MainPageLocators.INGREDIENT).click()

    def close_modal(self):
        self.driver.find_element(*MainPageLocators.MODAL_CLOSE).click()

    def add_ingredient_to_order(self):
        element = self.driver.find_element(*MainPageLocators.INGREDIENT)
        element.click() 
        self.close_modal()
        add_btn = element.find_element(By.XPATH, ".//button")
        add_btn.click()

    def get_ingredient_counter(self):
        return int(self.driver.find_element(*MainPageLocators.INGREDIENT_COUNTER).text)

    def modal_is_open(self):
        return self.driver.find_element(*MainPageLocators.MODAL).is_displayed()
