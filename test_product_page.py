import pytest
from pages.product_page import ProductPage

test_links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
              pytest.param(
                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                  marks=pytest.mark.xfail(reason="known issue")),
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]


@pytest.mark.parametrize('link', test_links)
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.product_should_be_added_to_basket()