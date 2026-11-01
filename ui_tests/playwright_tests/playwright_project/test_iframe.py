from pages.iframe_page import IframePage

def test_iframe_text_not_empty(page):
    iframe = IframePage(page)
    iframe.open()
    assert iframe.get_body_text() != ""

def test_iframe_page_heading(page):
    iframe = IframePage(page)
    iframe.open()
    assert "An iFrame" in iframe.get_page_heading()