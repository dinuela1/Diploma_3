from selenium.webdriver.common.by import By

class BasePageLocators:
    HEADER_CONSTRUCTOR = (By.LINK_TEXT, "Конструктор")
    HEADER_FEED = (By.LINK_TEXT, "Лента Заказов")
    HEADER_LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
