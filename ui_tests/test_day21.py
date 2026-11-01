import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES


#lesson 1
def test_successfull_login_with_webdrive(driver):
    wait = WebDriverWait(driver, 15)
    driver.get("https://the-internet.herokuapp.com/login")

    wait.until(ES.visibility_of_element_located((By.ID,"username"))).send_keys("tomsmith")
    wait.until(ES.visibility_of_element_located((By.ID, "password"))).send_keys("SuperSecretPassword!")
    wait.until(ES.element_to_be_clickable((By.CSS_SELECTOR, "button[type = 'submit']"))).click()
    message = wait.until(ES.visibility_of_element_located((By.CSS_SELECTOR, ".flash.success")))
    assert "You logged into a secure area!" in message.text

#lesson 2
def test_wrong_login_with_webdrive(driver):
    wait = WebDriverWait(driver, 15)
    driver.get("https://the-internet.herokuapp.com/login")

    wait.until(ES.visibility_of_element_located((By.ID, "username"))).send_keys("wrong")
    wait.until(ES.visibility_of_element_located((By.ID, "password"))).send_keys("wrong")
    wait.until(ES.element_to_be_clickable((By.CSS_SELECTOR, "button[type = 'submit']"))).click()
    message = wait.until(ES.visibility_of_element_located((By.CSS_SELECTOR, ".flash.error")))
    assert "Your username is invalid" in message.text

#lesson 3
def test_find_element(driver):
    driver.get("https://the-internet.herokuapp.com")
    element = driver.find_element(By.TAG_NAME, "h1")
    element.text
    assert "Welcome" in element.text

#lesson 4
def test_check_url_before_login(driver):
    wait = WebDriverWait(driver, 15)
    driver.get("https://the-internet.herokuapp.com/login")

    wait.until(ES.visibility_of_element_located((By.ID, "username"))).send_keys("tomsmith")
    wait.until(ES.visibility_of_element_located((By.ID, "password"))).send_keys("SuperSecretPassword!")
    wait.until(ES.element_to_be_clickable((By.CSS_SELECTOR, "button[type = 'submit']"))).click()
    wait.until(ES.url_contains("secure"))
    assert "secure" in driver.current_url


