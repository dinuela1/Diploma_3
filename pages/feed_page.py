from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage
from url import FEED_PAGE_URL


class FeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, FEED_PAGE_URL)

    def get_total_orders(self):
        return int(self.get_text(FeedPageLocators.TOTAL_ORDERS))

    def get_today_orders(self):
        return int(self.get_text(FeedPageLocators.TODAY_ORDERS))

    def get_in_progress_orders(self):
        elements = self.get_elements(FeedPageLocators.IN_PROGRESS_ORDERS)
        return [el.text for el in elements]
