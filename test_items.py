import pytest


url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_language(browser):
    browser.get(url)
    browser.find_element_by_css_selector('#add_to_basket_form')
