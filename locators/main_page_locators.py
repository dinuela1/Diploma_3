from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR = (By.LINK_TEXT, "Конструктор")
    FEED = (By.LINK_TEXT, "Лента Заказов")
    INGREDIENT = (By.XPATH, "//a[contains(@href, '/ingredient/')]")
    MODAL = (By.CLASS_NAME, "Modal_modal_opened__3ISw4")
    MODAL_CLOSE = (By.CLASS_NAME, "Modal_modal__close_modified__3V5XS")
    INGREDIENT_COUNTER = (By.CLASS_NAME, "counter_counter__num__3nue1")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
