import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def element_existence(browser):
    try:
        browser.implicitly_wait(10)
        browser.get(link)
        #browser.find_element_by_css_selector("wrong_selector")
        browser.find_element_by_css_selector("button.btn-add-to-basket")
        return True
    except:
        return False

def test_basket_button(browser):  
    assert element_existence(browser)==True, "Add to basket batton was not found"
    time.sleep(15)
    