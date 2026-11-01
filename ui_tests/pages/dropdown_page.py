from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class DropdownPage:
    DROPDOWN = (By.ID, "dropdown")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url = "https://the-internet.herokuapp.com/dropdown"):
        self.driver.get(url)

    def select_by_text(self, text):
        select_element = self.driver.find_element(*self.DROPDOWN)
        select = Select(select_element)
        select.select_by_visible_text(text)

    def select_by_index(self, index):
        select_element = self.driver.find_element(*self.DROPDOWN)
        select = Select(select_element)
        select.select_by_index(index)

    def get_selected_option(self):
        select = Select(self.driver.find_element(*self.DROPDOWN))
        return select.first_selected_option.text
    

