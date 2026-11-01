from pages.login_page import LoginPage
from pages.secure_page import SecurePage
import pytest

def test_successfull_login(page):
    login = LoginPage(page)
    login.open()
    login.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into"  in login.get_success_message()

def test_error_message(page):
    login = LoginPage(page)
    login.open()
    login.login("tomsmith", "test")
    assert "Your password is invalid!" in login.get_error_message()

def test_login_and_logout(page):
    login = LoginPage(page)
    login.open()
    login.login("tomsmith", "SuperSecretPassword!")

    secure = SecurePage(page)
    assert "Secure Area" in secure.get_heading()

    secure.logout()

    assert "login" in page.url


@pytest.mark.parametrize("username, password, expected_message",
[
    ("tomsmith", "SuperSecretPassword!", "You logged into"),
    ("wrong", "wrong", "Your username is invalid!"),
    ("tomsmith", "wrongpass", "Your password is invalid!"), 
])
def test_login_with_parametrize(page, username, password, expected_message):
    login = LoginPage(page)
    login.open()
    login.login(username, password)
    if "logged into" in expected_message:
        assert expected_message in page.text_content(".flash.success")
    else:
        assert expected_message in page.text_content(".flash.error")