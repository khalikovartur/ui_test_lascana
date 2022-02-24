import time
import pytest
from pom.adding_to_shopping_cart import ShoppingCart


def test_adding_into_shopping_cart(web_browser):

    page = ShoppingCart(web_browser)

    page.clothes_tab.click()
    page.first_product_picture.click()
    page.cookies.delete()

    # Getting the unique article of product
    product_article = page.uniq_product_article.get_text()
    page.button_add_to_cart.click()
    page.go_to_cart.click()

    current_url = page.get_current_url()
    assert current_url == "https://lascana.ru/personal/cart/"

    page.picture_product_in_the_cart.click()
    assert product_article == page.uniq_product_article.get_text()
