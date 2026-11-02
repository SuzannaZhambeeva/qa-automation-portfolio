import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = True)
        context = browser.new_context() 
        context.tracing.start(screenshots=True, snapshots=True) # ← начать запись
        page = context.new_page()
        yield page # ← тест получает page здесь
        context.tracing.stop(path="trace.zip") # ← сохранить запись
        browser.close()