class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page):
        self.page = page 

    def open(self):
        self.page.goto(self.URL)

    def login(self, username, password):
        self.page.get_by_label("Username").fill(username)
        self.page.get_by_label("Password").fill(password)
        self.page.get_by_role("button", name = "Login").click()

    def get_success_message(self):
        return self.page.text_content(".flash.success")

    def get_error_message(self):
        return self.page.text_content(".flash.error")

    
