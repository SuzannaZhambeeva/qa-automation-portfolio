from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#test 1 from test_login.py
def test_successful_login(driver):
    page = LoginPage(driver)
    page.open("https://the-internet.herokuapp.com/login")
    page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in page.get_success_message()

#test 2 from test_login.py
def test_wrong_login(driver):
    page = LoginPage(driver)
    page.open("https://the-internet.herokuapp.com/login")
    page.login("wrong", "SuperSecretPassword!")
    assert "Your username is invalid!" in page.get_error_message()

#test 3 from test_login.py
def test_login_and_logout(driver):
    login_page = LoginPage(driver)
    login_page.open("https://the-internet.herokuapp.com/login")
    login_page.login("tomsmith", "SuperSecretPassword!")

    WebDriverWait(driver, 10).until(EC.url_contains("secure"))
    secure_page = SecurePage(driver)
    assert "Secure Area" in secure_page.get_heading()

    secure_page.logout()

    assert "login" in driver.current_url
