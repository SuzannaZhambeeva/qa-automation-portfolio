from pages.alerts_page import AlertsPage

def test_js_alert(page):
    alerts = AlertsPage(page)
    alerts.open()
    page.once("dialog", lambda dialog: dialog.accept())
    alerts.click_alert()
    assert "You successfully clicked an alert" in alerts.get_result()

def test_js_confirm(page):
    alerts = AlertsPage(page)
    alerts.open()
    page.once("dialog", lambda dialog: dialog.dismiss())
    alerts.click_confirm()
    assert "You clicked: Cancel" in alerts.get_result()

def test_prompt(page):
    alerts = AlertsPage(page)
    alerts.open()
    page.once("dialog", lambda dialog: dialog.accept("Hello Playwright"))
    alerts.click_prompt()
    assert "Hello Playwright" in alerts.get_result()