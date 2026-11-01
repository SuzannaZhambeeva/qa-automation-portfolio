from pages.dropdown_page import DropdownPage

def test_select_by_text(page):
    dropdown = DropdownPage(page)
    dropdown.open()
    dropdown.select_by_text("Option 1")
    assert dropdown.get_selected_value() == "1"

def test_select_by_index(page):
    dropdown = DropdownPage(page)
    dropdown.open()
    dropdown.select_by_index(2)
    assert dropdown.get_selected_value() == "2"
    
def test_dropdown_default_value(page):
    dropdown = DropdownPage(page)
    dropdown.open()
    assert dropdown.get_selected_value() == ""
