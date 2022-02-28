How To Run Tests

1)In your terminale line:
$ git clone https://github.com/khalikovartur/ui_tests_lascana.git

#cd ui_tests_lascana
#mkvirtualenv

2)Install all requirements in terminal: 
$ pip3 install -r requirements.txt

3)Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

#$ mkdir chromedriver
#exstract to chromdriver folder


4)Run tests in terminal: $ python3 -m pytest -v --driver Chrome --driver-path "xpath to your chromedriver"

5)For 'allure' report run test in terminal with flag:  $ python3 -m pytest -v --alluredir=allurelog --driver Chrome --driver-path "xpath to your chromedriver"

6)For show 'allure' repot : $ allure serve allurelog/

7)For show screenshots: $ mkdir screenshots