class IframePage:
    URL = "https://the-internet.herokuapp.com/iframe"

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def get_body_text(self):
        frame = self.page.frame_locator("#mce_0_ifr")
        return frame.locator("body").inner_text()

    def get_page_heading(self):
        return self.page.locator("h3").text_content()
    
