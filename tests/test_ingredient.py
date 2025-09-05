import allure
from pages.main_page import MainPage


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
    assert new_count == (initial_count + 1)
