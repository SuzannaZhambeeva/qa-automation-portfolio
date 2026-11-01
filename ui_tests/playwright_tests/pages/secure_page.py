class SecurePage:

    def __init__(self, page):
        self.page = page

    def get_heading(self):
        heading = self.page.get_by_role("heading").first
        return heading.text_content()

    def logout(self):
        self.page.get_by_role("link", name = "Logout").click()