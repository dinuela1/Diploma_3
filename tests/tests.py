import allure
import time
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from tests.conftest import create_order


@allure.title("Переход по клику на Конструктор")
def test_click_constructor(driver):
    page = MainPage(driver)
    page.open()
    page.click_constructor()
    assert "burger" in driver.current_url


@allure.title("Переход по клику на Ленту заказов")
def test_click_feed(driver):
    page = MainPage(driver)
    page.open()
    page.click_feed()
    assert "feed" in driver.current_url


@allure.title("Открытие и закрытие модального окна ингредиента")
def test_ingredient_modal(driver):
    page = MainPage(driver)
    page.open()
    page.click_ingredient()
    assert page.modal_is_open()
    page.close_modal()


@allure.title("При добавлении ингредиента счётчик увеличивается")
def test_add_ingredient_counter(driver):
    page = MainPage(driver)
    page.open()
    initial_count = page.get_ingredient_counter()
    page.add_ingredient_to_order()
    new_count = page.get_ingredient_counter()
    assert new_count == initial_count + 1


@allure.title("После создания заказа 'выполнено за все время' увеличивается")
def test_total_orders_increases(driver, user_token):
    page = FeedPage(driver)
    page.open()
    before = page.get_total_orders()
    create_order(user_token, ["61c0c5a71d1f82001bdaaa6d"])
    time.sleep(2)
    driver.refresh()
    after = page.get_total_orders()
    assert after > before


@allure.title("После создания заказа 'выполнено за сегодня' увеличивается")
def test_today_orders_increases(driver, user_token):
    page = FeedPage(driver)
    page.open()
    before = page.get_today_orders()
    create_order(user_token, ["61c0c5a71d1f82001bdaaa6d"])
    time.sleep(2)
    driver.refresh()
    after = page.get_today_orders()
    assert after > before


@allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
def test_order_number_in_progress(driver, user_token):
    resp = create_order(user_token, ["61c0c5a71d1f82001bdaaa6d"])
    order_number = str(resp.json()["order"]["number"])
    page = FeedPage(driver)
    page.open()
    time.sleep(2)
    driver.refresh()
    in_progress = page.get_in_progress_orders()
    assert any(order_number in order for order in in_progress)
