from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IframePage:
    IFRAME = (By.ID, "mce_0_ifr")
    BODY   = (By.TAG_NAME, "body")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url = "https://the-internet.herokuapp.com/iframe"):
        self.driver.get(url)

    def switch_to_iframe(self):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "mce_0_ifr")))

    def get_body_content(self):
        body = self.driver.find_element(*self.BODY)
        return body.get_attribute ("innerHTML") 

    def switch_to_main(self):
        self.driver.switch_to.default_content()
