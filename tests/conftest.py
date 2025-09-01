import pytest
from selenium import webdriver
import requests
from url import *


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        d = webdriver.Chrome(options=options)
    else:
        options = webdriver.FirefoxOptions()
        d = webdriver.Firefox(options=options)
    d.maximize_window()
    yield d
    d.quit()


@pytest.fixture
def current_url(driver):
    return driver.current_url


@pytest.fixture
def user_token(new_user):
    return new_user["token"]


def create_order(token=None, ingredients=None):
    headers = {"Authorization": token} if token else {}
    body = {"ingredients": ingredients} if ingredients else {}
    return requests.post(f"{BASE_URL}/orders", headers=headers, json=body)
