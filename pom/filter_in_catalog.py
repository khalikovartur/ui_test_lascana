from pom.base import WebPage
from pom.elements import WebElement, ManyWebElements


class FilterProduct(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://lascana.ru/'
        super().__init__(web_driver, url)

    underwear_tab = WebElement(css_selector='li.navigation-menu__item:nth-child(2) > a:nth-child(1)')
    min_cost_input = WebElement(id='arrFilter_P1_MIN')
    max_cost_input = WebElement(id='arrFilter_P1_MAX')
    red_color = WebElement(css_selector='label.checkbox-pictures__label:nth-child(7)')
    set_filter = WebElement(id='set_filter')
    items_cost = ManyWebElements(class_name='product-card__price-block')
