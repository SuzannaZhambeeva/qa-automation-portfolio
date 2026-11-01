from playwright.sync_api import sync_playwright
import pytest

def test_login_success(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.click("button[type='submit']")
    assert "You logged into" in page.text_content(".flash.success")

def test_login_success2(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    assert "You logged into" in page.text_content(".flash.success")

@pytest.mark.parametrize("username, password, expected_message",[
    ("tomsmith", "SuperSecretPassword!", "You logged into"),
    ("wrong", "wrong", "Your username is invalid!"),
    ("tomsmith", "wrongpass", "Your password is invalid!"), 
])
def test_login_success_with_parametrize(page, username, password, expected_message):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill(username)
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name="Login").click()
    if "logged into" in expected_message:
        assert expected_message in page.text_content(".flash.success")
    else:
        assert expected_message in page.text_content(".flash.error")
    
def test_check_head(page):
    page.goto("https://the-internet.herokuapp.com")
    #page.get_by_role("heading")
    heading = page.get_by_role("heading").first
    assert "Welcome" in heading.text_content()