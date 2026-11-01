from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

class LoginPage:
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MSG = (By.CSS_SELECTOR, ".flash.success")
    ERROR_MSG = (By.CSS_SELECTOR, ".flash.error")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url = "https://the-internet.herokuapp.com/login"):
        self.driver.get(url)
    
    def login(self, username, password):
        self.wait.until(ES.visibility_of_element_located(self.USERNAME)).send_keys(username)
        self.wait.until(ES.visibility_of_element_located(self.PASSWORD)).send_keys(password)
        self.wait.until(ES.element_to_be_clickable(self.BUTTON)).click()

    def get_success_message(self):
        return self.wait.until(ES.visibility_of_element_located(self.SUCCESS_MSG)).text
    
    def get_error_message(self):
        return self.wait.until(ES.visibility_of_element_located(self.ERROR_MSG)).text
    