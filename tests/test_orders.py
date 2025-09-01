import allure
from pages.feed_page import FeedPage
from tests.conftest import create_order


@allure.title("После создания заказа 'выполнено за все время' увеличивается")
def test_total_orders_increases(driver, user_token):
    page = FeedPage(driver)
    page.open()
    before = page.get_total_orders()
    create_order(user_token, ["61c0c5a71d1f82001bdaaa6d"])
    after = page.get_total_orders()
    assert after > before


@allure.title("После создания заказа 'выполнено за сегодня' увеличивается")
def test_today_orders_increases(driver, user_token):
    page = FeedPage(driver)
    page.open()
    before = page.get_today_orders()
    create_order(user_token, ["61c0c5a71d1f82001bdaaa6d"])
    after = page.get_today_orders()
    assert after > before


@allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
def test_order_number_in_progress(driver, user_token):
    resp = create_order(user_token, ["61c0c5a71d1f82001bdaaa6d"])
    order_number = str(resp.json()["order"]["number"])
    page = FeedPage(driver)
    page.open()
    in_progress = page.get_in_progress_orders()
    assert any(order_number in order for order in in_progress)
