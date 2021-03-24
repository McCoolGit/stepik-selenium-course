import pytest
import time


def test_add_to_cart(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    assert browser.find_element_by_class_name("btn-add-to-basket")
