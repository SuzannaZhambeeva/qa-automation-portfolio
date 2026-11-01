import pytest
from playwright.sync_api import sync_playwright

def test_open_page():
        with sync_playwright() as p:
            browser = p.chromium.launch(headless = False)
            page = browser.new_page()
            page.goto("https://the-internet.herokuapp.com")
            assert "The Internet" in page.title()
            browser.close()


def test_opne_page_with_fixture(page):
      page.goto("https://the-internet.herokuapp.com")
      assert "The Internet" in page.title()

def test_login_success(page):
      page.goto("https://the-internet.herokuapp.com/login")
      page.fill("#username", "tomsmith")
      page.fill("#password", "SuperSecretPassword!")
      page.click("button[type='submit']")
      assert "You logged into" in page.text_content(".flash.success")

def test_login_unsuccess(page):
      page.goto("https://the-internet.herokuapp.com/login")
      page.fill("#username", "test")
      page.fill("#password", "test")
      page.click("button[type='submit']")
      assert "Your username is invalid!" in page.text_content(".flash.error")

