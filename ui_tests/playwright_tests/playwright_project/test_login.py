from pages.login_page import LoginPage
from pages.secure_page import SecurePage

def test_successful_login(page):
    login = LoginPage(page)
    login.open()
    login.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into" in login.get_success_message()

def test_wrong_login(page):
    login = LoginPage(page)
    login.open()
    login.login("wrong", "wrong")
    assert "Your username is invalid!" in login.get_error_message()

def test_login_and_logout(page):
    login = LoginPage(page)
    login.open()
    login.login("tomsmith", "SuperSecretPassword!")
    secure = SecurePage(page)
    assert "Secure Area" in secure.get_heading()
    secure.logout()
    assert "login" in page.url


