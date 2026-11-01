# # conftest.py
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome(
#         service=Service(ChromeDriverManager().install())
#     )
#     driver.implicitly_wait(10)
#     yield driver        # ← тест получает driver здесь
#     driver.quit()       # ← браузер закрывается после теста

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    service = Service("/Users/suzanna.zhambeeva99/.wdm/drivers/chromedriver/mac64/152.0.7977.82/chromedriver-mac-arm64/chromedriver")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()