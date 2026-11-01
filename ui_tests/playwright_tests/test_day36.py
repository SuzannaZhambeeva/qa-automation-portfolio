from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright


# def test_example(page: Page) -> None:
#     page.goto("https://the-internet.herokuapp.com/login")
#     page.get_by_label("Username").fill("tomsmith")
#     page.get_by_label("Password").fill("SuperSecretPassword!")
#     page.get_by_role("button", name="Login").click()
#     assert "You logged into" in page.text_content(".flash.success")

def test_login_success(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("test")
    page.click("button[type='submit']")
    try:
        assert "You logged into" in page.text_content(".flash.success")
    except Exception:
        page.screenshot(path="fail.png")
        raise
