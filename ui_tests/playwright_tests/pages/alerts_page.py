class AlertsPage:
    URL = "https://the-internet.herokuapp.com/javascript_alerts"

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def click_alert(self):
        self.page.get_by_role("button", name="Click for JS Alert").click()

    def click_confirm(self):
        self.page.get_by_role("button", name="Click for JS Confirm").click()

    def click_prompt(self):
        self.page.get_by_role("button", name="Click for JS Prompt").click()

    def get_result(self):
        return self.page.locator("#result").text_content()


    