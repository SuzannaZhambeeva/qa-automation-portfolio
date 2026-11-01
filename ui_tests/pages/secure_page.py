from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

class SecurePage:
    HEADING = (By.TAG_NAME, "h2")
    LOGOUT_BTN = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_heading(self):
        return self.wait.until(ES.visibility_of_element_located(self.HEADING)).text

    def logout(self):
        self.wait.until(ES.element_to_be_clickable(self.LOGOUT_BTN)).click()
