from selenium.webdriver.common.by import By


class FeedPageLocators:
    TOTAL_ORDERS = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    IN_PROGRESS_ORDERS = (By.CLASS_NAME, "OrderFeed_orderListReady__1YFgp")
