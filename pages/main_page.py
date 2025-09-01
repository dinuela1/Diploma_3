from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from url import MAIN_PAGE_URL
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, MAIN_PAGE_URL)
    def click_ingredient(self):
        self.click(MainPageLocators.INGREDIENT)

    def close_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE)

    def add_ingredient_to_order(self):
        element = self.wait_for_element(MainPageLocators.INGREDIENT)
        add_btn = element.find_element(By.XPATH, ".//button")
        add_btn.click()

    def get_ingredient_counter(self):
        return int(self.get_text(MainPageLocators.INGREDIENT_COUNTER))

    def modal_is_open(self):
        return self.is_visible(MainPageLocators.MODAL)

    def click_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON)
