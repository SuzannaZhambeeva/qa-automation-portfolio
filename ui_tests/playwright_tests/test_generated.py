from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name=" Login").click()
