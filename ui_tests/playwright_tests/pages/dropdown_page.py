class DropdownPage:
    URL = "https://the-internet.herokuapp.com/dropdown"

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def select_by_text(self, text):
        self.page.select_option("#dropdown", label = text)

    def select_by_index(self, index):
        self.page.select_option("#dropdown", index=index)

    def get_selected_value(self):
        return self.page.locator("#dropdown").input_value()
    