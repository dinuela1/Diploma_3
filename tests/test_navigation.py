import allure
from pages.main_page import MainPage


@allure.title("Переход по клику на Конструктор")
def test_click_constructor(driver):
    page = MainPage(driver)
    page.open()
    page.click_constructor()
    assert "burger" in page.current_url()


@allure.title("Переход по клику на Ленту заказов")
def test_click_feed(driver):
    page = MainPage(driver)
    page.open()
    page.click_feed()
    assert "feed" in page.current_url()
