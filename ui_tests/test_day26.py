import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as ES




ALERT_BTN = (By.XPATH, "//button[text()='Click for JS Alert']")
CONFIRM_BTN = (By.XPATH, "//button[text()='Click for JS Confirm']")
PROMPT_BTN = (By.XPATH, "//button[text()='Click for JS Prompt']")

#lesson 1 alert
def test_js_alert(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    wait = WebDriverWait(driver, 10)
    wait.until(ES.element_to_be_clickable(ALERT_BTN)).click()
    alert = wait.until(ES.alert_is_present())
    alert.accept()
    RESULT = (By.ID, "result")
    result_text = wait.until(ES.visibility_of_element_located(RESULT)).text

    assert "You successfully clicked an alert" in result_text

#lesson 1 confirm
def test_confirm(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    wait = WebDriverWait(driver, 30)
    wait.until(ES.element_to_be_clickable(CONFIRM_BTN)).click()
    alert = wait.until(ES.alert_is_present())
    alert.dismiss()
    time.sleep(2)
    RESULT = (By.ID, "result")
    result_text = wait.until(ES.visibility_of_element_located(RESULT)).text

    assert "You clicked: Cancel" in result_text

#lesson 1 prompt
def test_prompt(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    wait = WebDriverWait(driver, 30)
    wait.until(ES.element_to_be_clickable(PROMPT_BTN)).click()
    alert = wait.until(ES.alert_is_present())
    alert.send_keys("Hello")
    alert.accept()
    time.sleep(3)
    RESULT = (By.ID, "result")
    result_text = wait.until(ES.visibility_of_element_located(RESULT)).text
    

    assert  "Hello" in result_text

#lesson 2
def test_iframe(driver):
    driver.get("https://the-internet.herokuapp.com/iframe")

    driver.switch_to.frame("mce_0_ifr")
    body = driver.find_element(By.TAG_NAME, "body")
    assert body.is_displayed()
    content = body.get_attribute("innerHTML")           # читаем содержимое
    assert content != "" 
    driver.switch_to.default_content()


#lesson 3
def test_scroll(driver):
    driver.get("https://the-internet.herokuapp.com/infinite_scroll")

    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(2)

    assert "infinite_scroll" in driver.current_url

#lesson 4
def test_select(driver):
    driver.get("https://the-internet.herokuapp.com/dropdown")

    select_element = driver.find_element(By.ID, "dropdown")
    select = Select(select_element)

    select.select_by_visible_text("Option 1")
    assert select.first_selected_option.text == "Option 1"

    select.select_by_visible_text("Option 2")
    assert select.first_selected_option.text == "Option 2"

#lesson 1 api Тест 1. GET /users/4 — статус 200, id == 4, first_name не пустой.
def test_check_user(api_client, base_url):
    response = api_client.get(
    f"{base_url}/users/4"
)
    assert response.status_code == 200

    body = response.json()
    user = body["data"]
    assert user["id"] == 4

    assert user["first_name"] != ""

#lesson 2 Тест 2. Параметризованный DELETE для пользователей 4, 5, 6 — статус 204.
@pytest.mark.parametrize("id", [(4), (5), (6)])
def test_delete_user(api_client, base_url, id):
    response = api_client.delete(
        f"{base_url}/users/{id}"
    )

    assert response.status_code == 204