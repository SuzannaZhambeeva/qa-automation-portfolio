from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

#lesson 1
def test_open_page():
    driver =  webdriver.Chrome(
        service = Service(ChromeDriverManager().install())
    )

    driver.get("https://the-internet.herokuapp.com")

    assert "The Internet" in driver.title

    driver.quit()

#lesson 2
def test_open_driver_with_fixture(driver):
    driver.get("https://the-internet.herokuapp.com")
    time.sleep(2)
    assert "The Internet" in driver.title

#lesson 3
def test_check_driver_title(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(2)
    assert "The Internet" in driver.title 
    assert "login" in driver.current_url
