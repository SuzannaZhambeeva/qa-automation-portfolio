from pages.login_page import LoginPage
from pages.secure_page import SecurePage
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

#lesson 2/1
def test_successful_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in page.get_success_message()

#lesson 2/2
def test_wrong_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("wrong", "wrong")
    assert "Your username is invalid!" in page.get_error_message()

#leson 2/3
@pytest.mark.parametrize("username, password, success",[
    ("tomsmith", "SuperSecretPassword!", True),
    ("wrong", "wrong", False),
    ("tomsmith", "wrongpass", False), 
])
def test_login_with_parametrize(driver, username, password, success):
    page = LoginPage(driver)
    page.open()
    page.login(username, password)
    if success == "succecc":
        assert "You logged into a secure area!" in page.get_success_message()
    if success == "invalid_username" :
        assert "Your username is invalid!" in page.get_error_message()
    elif success == "invalid_password":
        assert "Your password is invalid!" in page.get_error_message()

#lesson 3
def test_login_and_logout(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    WebDriverWait(driver, 10).until(EC.url_contains("secure"))

    secure_page = SecurePage(driver)
    assert "Secure Area" in secure_page.get_heading()

    secure_page.logout()

    assert "login" in driver.current_url

#api test 1
#Тест 1. POST создать пользователя "Kate" / "QA" — статус и name == "Kate".
def test_create_user(api_client, base_url):
    response = api_client.post(
        f"{base_url}/users",
        json={"name":"Kate", "job": "QA"}
        )

    assert response.status_code == 201    
    body = response.json()
    print(body)
    assert body["name"] == "Kate"
    assert body["job"] == "QA"

#api test 2
#Тест 2. GET параметризованный для страниц 1 и 2 — статус 200 и page совпадает с параметром.
@pytest.mark.parametrize("page", [1, 2])
def test_check_user(api_client, base_url, page):
    response = api_client.get(
        f"{base_url}/users?page={page}"
    )
    assert response.status_code == 200
    body = response.json()

    assert page == body["page"]
    