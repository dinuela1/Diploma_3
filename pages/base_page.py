from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 5)

    def open(self):
        self.driver.get(self.url)

    def wait_for_element(self, locator):
         return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def scroll_to(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    def click(self, locator):
        self.wait_for_element_clickable(locator).click()

    def get_text(self, locator):
        return self.wait_for_element(locator).text

    def is_visible(self, locator):
        return self.wait_for_element(locator).is_displayed()

    def click_constructor(self):
        self.click(BasePageLocators.HEADER_CONSTRUCTOR)

    def click_feed(self):
        self.click(BasePageLocators.HEADER_FEED)

    def click_logo(self):
        self.click(BasePageLocators.HEADER_LOGO)
