import pytest


url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_basket_button(browser):
    browser.get(url)
    buttons = browser.find_elements_by_css_selector('#add_to_basket_form')
    assert len(buttons) > 0, 'Кнопки нет'
