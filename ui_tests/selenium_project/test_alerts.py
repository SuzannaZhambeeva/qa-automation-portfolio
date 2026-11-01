from pages.alerts_page import AlertsPage
from selenium.webdriver.support import expected_conditions as EC

#test 1 js alert
def test_js_alert(driver):
    page = AlertsPage(driver)
    page.open("https://the-internet.herokuapp.com/javascript_alerts")
    page.click_alert()
    alert = page.wait.until(EC.alert_is_present())
    alert.accept()

    assert "You successfully clicked an alert" in page.get_result()

#test 2 js confirm
def test_js_confirm(driver):
    page = AlertsPage(driver)
    page.open("https://the-internet.herokuapp.com/javascript_alerts")
    page.click_confirm()
    alert = page.wait.until(EC.alert_is_present())
    alert.dismiss()

    assert "You clicked: Cancel" in page.get_result()

#test 3 js prompt
def test_js_prompt(driver):
    page = AlertsPage(driver)
    page.open("https://the-internet.herokuapp.com/javascript_alerts")
    page.click_prompt()
    alert = page.wait.until(EC.alert_is_present())
    alert.send_keys("Hello Selenium")
    alert.accept()

    assert "Hello Selenium" in page.get_result()


