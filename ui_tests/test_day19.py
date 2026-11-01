import pytest
from selenium.webdriver.common.by import By
import time

#lesson 1
def test_find_element(driver):
    driver.get("https://the-internet.herokuapp.com")
    time.sleep(2)
    element = driver.find_element(By.TAG_NAME, "h1")
    element.text
    assert "Welcome" in element.text

#lesson 2
def test_succesessfull_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(2)
    element_login = driver.find_element(By.ID, "username")
    element_login.send_keys("tomsmith")
    element_password = driver.find_element(By.ID, "password")
    element_password.send_keys("SuperSecretPassword!")
    element_button = driver.find_element(By.CSS_SELECTOR, "button[type = 'submit']")
    element_button.click()
    element_sucessfull = driver.find_element(By.CSS_SELECTOR, ".flash.success")
    assert "You logged into a secure area!" in element_sucessfull.text

#lesson 3
def test_wrong_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(5)
    element_login = driver.find_element(By.ID, "username")
    element_login.send_keys("wrong")
    element_password = driver.find_element(By.ID, "password")
    element_password.send_keys("wrong")
    time.sleep(2)
    element_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    element_button.click()
    time.sleep(2)
    element_wrong = driver.find_element(By.CSS_SELECTOR, ".flash.error")
    assert "Your username is invalid!" in element_wrong.text
    time.sleep(2)

#lesson 4
@pytest.mark.parametrize("username, password, success",[
    ("tomsmith", "SuperSecretPassword!", True),
    ("wrong", "wrong", False),
    ("tomsmith", "wrongpass", False), 
])
def test_login_with_parametrize(driver, username, password, success):
    driver.get("https://the-internet.herokuapp.com/login")
    element_login = driver.find_element(By.ID, "username")
    element_login.send_keys(username)
    element_password = driver.find_element(By.ID, "password")
    element_password.send_keys(password)
    time.sleep(2)
    element_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    time.sleep(2)
    element_button.click()
    if success == "success":
        message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
        assert "You logged into a secure area!" in message.text
    elif success == "invalid_username" :
        message = driver.find_element(By.CSS_SELECTOR, ".flash.error")
        assert "Your username is invalid!" in message.text
    elif success == "invalid_password" :
        message = driver.find_element(By.CSS_SELECTOR, ".flash.error")
        assert "Your password is invalid!" in message.text
    time.sleep(2)

#lesson api 1
def test_check_status(api_client, base_url):
    response = api_client.get(
        f"{base_url}/users/5"
    )

    assert response.status_code == 200
    body = response.json()
    user = body["data"]
    assert user ["id"] == 5

    assert "@" in user["email"]


#lesson api 2
@pytest.mark.parametrize("id", [
    (1),
    (2),
    (3)
])
def test_check_status_with_parametrize(api_client, base_url, id):
    response = api_client.delete(
        f"{base_url}/users/{id}"
    )

    assert response.status_code == 204

#lesson api for 18 day
def test__check_status(api_client, base_url):
    response = api_client.get(
        f"{base_url}/users?page=2",
    )
    
    assert response.status_code == 200

    body = response.json()
    user = body["data"]

    assert body["page"] == 2
    assert len(user) > 0

