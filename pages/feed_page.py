from locators.feed_page_locators import FeedPageLocators


class FeedPage:
    URL = "https://stellarburgers.nomoreparties.site/feed"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def get_total_orders(self):
        return int(self.driver.find_element(*FeedPageLocators.TOTAL_ORDERS).text)

    def get_today_orders(self):
        return int(self.driver.find_element(*FeedPageLocators.TODAY_ORDERS).text)

    def get_in_progress_orders(self):
        return [el.text for el in self.driver.find_elements(*FeedPageLocators.IN_PROGRESS_ORDERS)]
