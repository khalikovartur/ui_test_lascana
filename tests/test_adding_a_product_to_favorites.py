import pytest
from pom.adding_to_favorites import FavoritesProducts


def test_adding_into_favorites(web_browser):
    """The test adds to favorites and checks the favorites on the favorites' page with the article number."""

    page = FavoritesProducts(web_browser)

    page.kupalniki_tab.click()
    page.first_picture.click()
    page.cookies.delete()
    page.discount_frame.delete()
    page.icon_add_to_favorites.scroll_to_element()
    page.icon_add_to_favorites.click()
    # Get the article from the liked product
    item_article = page.uniq_product_article.get_text()

    # Go to favorites
    page.header_link_into_favorites.click()
    assert page.get_current_url() == 'https://lascana.ru/personal/favorite/'


    page.favorites_item_image.click()
    assert item_article == page.uniq_product_article.get_text()


