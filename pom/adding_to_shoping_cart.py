from pom.base import WebPage
from pom.elements import WebElement


class FavoritesPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://lascana.ru/'
        super().__init__(web_driver, url)