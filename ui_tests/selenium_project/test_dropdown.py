from pages.dropdown_page import DropdownPage

def test_choose_drop_1(driver):
    page = DropdownPage(driver)
    page.open("https://the-internet.herokuapp.com/dropdown")
    page.select_by_text("Option 1")
    assert page.get_selected_option() == "Option 1"

def test_choose_drop_2(driver):
    page = DropdownPage(driver)
    page.open("https://the-internet.herokuapp.com/dropdown")
    page.select_by_index(2)
    assert page.get_selected_option() == "Option 2"
