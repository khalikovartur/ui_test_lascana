import time
import pytest
from pom.adding_to_shopping_cart import ShoppingCart


def test_adding_into_shopping_cart(web_browser):
    """The test adds to the shopping cart and checks the product on the carts' page with the article number."""

    page = ShoppingCart(web_browser)

    page.clothes_tab.click()
    page.first_product_picture.click()
    page.cookies.delete()
    page.discount_frame.delete()

    # Getting the unique article of product
    product_article = page.uniq_product_article.get_text()
    page.button_add_to_cart.click()
    page.go_to_cart.click()

    current_url = page.get_current_url()
    assert current_url == "https://lascana.ru/personal/cart/"

    page.picture_product_in_the_cart.click()
    assert product_article == page.uniq_product_article.get_text()
