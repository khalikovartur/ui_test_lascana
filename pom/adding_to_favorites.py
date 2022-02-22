from pom.base import WebPage
from pom.elements import WebElement


class FavoritesPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://lascana.ru/'
        super().__init__(web_driver, url)

    cookies = WebElement(css_selector='body > div.cookie-popup > div')
    kupalniki_tab = WebElement(css_selector='li.navigation-menu__item:nth-child(4) > a:nth-child(1)')
    first_picture = WebElement(xpath='/html/body/section/div[4]/div/div/div[1]/a/div[1]')
    icon_add_to_favorites = WebElement(css_selector='a.link:nth-child(17)')
    uniq_product_article = WebElement(id='product__article')
    header_link_into_favorites = WebElement(css_selector='.header-links__favourites')
    # discount_window = WebElement(css_selector='.discounts-popup')
    favorites_item_image = WebElement(css_selector='.personal__favorite--item_image')