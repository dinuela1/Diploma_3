import allure
from pages.main_page import MainPage


@allure.title("Переход по клику на Конструктор")
def test_click_constructor(driver, current_url):
    page = MainPage(driver)
    page.open()
    page.click_constructor()
    assert "burger" in current_url


@allure.title("Переход по клику на Ленту заказов")
def test_click_feed(driver, current_url):
    page = MainPage(driver)
    page.open()
    page.click_feed()
    assert "feed" in current_url
    