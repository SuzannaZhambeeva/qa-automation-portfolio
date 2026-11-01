from pages.iframe_page import IframePage
from selenium.webdriver.common.by import By

def test_iframe(driver):
    page = IframePage(driver)
    page.open("https://the-internet.herokuapp.com/iframe")
    page.switch_to_iframe()
    assert page.get_body_content() != ""
    page.switch_to_main()

def test_iframe_2(driver):
    page = IframePage(driver)
    page.open("https://the-internet.herokuapp.com/iframe")
    page.switch_to_iframe()
    page.switch_to_main()
    element = driver.find_element(By.TAG_NAME, "h3")
    assert "An iFrame" in element.text



