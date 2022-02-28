from pom.base import WebPage
from pom.elements import WebElement


class FavoritesProducts(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://lascana.ru/'
        super().__init__(web_driver, url)

    cookies = WebElement(css_selector='body > div.cookie-popup > div')
    discount_frame = WebElement(xpath='//*[@id="top-modal"]/div')
    kupalniki_tab = WebElement(css_selector='li.navigation-menu__item:nth-child(4) > a:nth-child(1)')
    first_picture = WebElement(xpath='/html/body/section/div[4]/div/div/div[1]/a/div[1]')
    #icon_add_to_favorites = WebElement(css_selector='a.link:nth-child(17)')
    icon_add_to_favorites = WebElement(xpath='/html/body/section/div[2]/div[2]/div[4]/a[3]')
    uniq_product_article = WebElement(id='product__article')
    header_link_into_favorites = WebElement(css_selector='.header-links__favourites')
    favorites_item_image = WebElement(css_selector='.personal__favorite--item_image')