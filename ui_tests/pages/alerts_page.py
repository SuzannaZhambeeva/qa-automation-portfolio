from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AlertsPage:
    ALERT_BTN = (By.XPATH, "//button[text()='Click for JS Alert']")
    CONFIRM_BTN = (By.XPATH, "//button[text()='Click for JS Confirm']")
    PROMPT_BTN = (By.XPATH, "//button[text()='Click for JS Prompt']")
    RESULT = (By.ID, "result")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url = "https://the-internet.herokuapp.com/javascript_alerts"):
        self.driver.get(url)

    def click_alert(self):
        self.wait.until(EC.element_to_be_clickable(self.ALERT_BTN)).click()

    def click_confirm(self):
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_BTN)).click()

    def click_prompt(self):
        self.wait.until(EC.element_to_be_clickable(self.PROMPT_BTN)).click()

    def get_result(self):
        return self.wait.until(EC.visibility_of_element_located(self.RESULT)).text
    
    

