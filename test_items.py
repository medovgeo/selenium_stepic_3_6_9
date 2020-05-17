import time


def test_add_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    # time.sleep(7)
    button = len(browser.find_elements_by_class_name('btn-add-to-basket'))
    assert button == 1, f"Expected to find 1 'Add to basket' button, found: {button}"
