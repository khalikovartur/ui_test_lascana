from pom.base import WebPage
from pom.elements import WebElement


class RegisPage(WebPage):
    
    def __init__(self, web_driver, url=''):
        url = 'https://lascana.ru/'
        super().__init__(web_driver, url)   
        
    user_icon = WebElement(css_selector='.header-links__account')
    #user_icon = WebElement(xpath='/html/body/header/div[2]/div/div[3]/a[2]')
    
    regis_link = WebElement(css_selector='#auth_form > div > div:nth-child(2) > a')
    
    cookies = WebElement(css_selector='body > div.cookie-popup > div')
    
    last_name = WebElement(css_selector='#register_form > label:nth-child(6) > input')
    name = WebElement(css_selector='#register_form > label:nth-child(7) > input')
    email = WebElement(css_selector='#register_form > label:nth-child(9) > input')
    password = WebElement(css_selector='#register_form > label:nth-child(11) > input')
    confirm_password = WebElement(css_selector='#register_form > label:nth-child(12) > input') 
    
    agreement=WebElement(id='register_personal')
    agreement_box=WebElement(css_selector='.checkbox-personal > span:nth-child(2)')
    
    regis_button=WebElement(css_selector='.register-buttons__submit-button')
    
    
class AuthPage(WebPage):
    
    def __init__(self, web_driver, url=''):
        url = 'https://lascana.ru/'
        super().__init__(web_driver, url) 
        
    user_icon = WebElement(css_selector='.header-links__account')
    
    email = WebElement(css_selector='#auth_form > label:nth-child(3) > input')
    password = WebElement(css_selector='#auth_form > label:nth-child(4) > div > input')
    auth_submit_button = WebElement(css_selector='#auth_form > div > input')
    
    name_header_link = WebElement(class_name='header-links__name')


