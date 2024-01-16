import os
from QA2823.Alina_Gomonova.Class_Work.New_Dyploma_Alina.pages.base_page import WebPage
from QA2823.Alina_Gomonova.Class_Work.New_Dyploma_Alina.pages.elements import WebElement
from QA2823.Alina_Gomonova.Class_Work.New_Dyploma_Alina.pages.elements import ManyWebElements


class FuterBtn(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("FUTER") or 'https://www.onliner.by/'

        super().__init__(web_driver, url)

    # О компании
    btn_futer_about = WebElement(xpath='//footer//a[@href="https://blog.onliner.by/about"]')

    # Контакты редакции
    btn_futer_contacts = WebElement(xpath='//footer//a[@href="https://people.onliner.by/contacts"]')

    # Инпут быстрого поиска на главной страницы
    input_fast_search = WebElement(xpath='//input[@class="fast-search__input"]')

    # Вывод результата поиска
    count_fast_search_result = ManyWebElements(xpath='//li[@class="b-main-navigation__item b-main-navigation__item_arrow"]')

    # Вывод результата поиска
    btn_button = WebElement(css_selector='a[class="yt-simple-endpoint style-scope ytd-topbar-menu-button-renderer"]')

    # Вывод результата поиска
    btn_endpoint = WebElement(xpath='(//div[@id="primary-text-container"])[7]')

    # Вывод результата поиска
    btn_close = WebElement(css_selector='button[class="help-panel-header__close-button"]')


from selenium.webdriver.common.by import By

stock_stories_button = (By.XPATH, '(//img[@class="stories-circle__image"])[2]')
life_stories_button = (By.XPATH, '(//img[@class="stories-circle__image"])[3]')
hits_stories_button = (By.XPATH, '(//img[@class="stories-circle__image"])[4]')
darling_stories_button = (By.XPATH, '(//img[@class="stories-circle__image"])[5]')
for_me_stories_button = (By.XPATH, '(//img[@class="stories-circle__image"])[6]')
news_stories_button = (By.XPATH, '(//img[@class="stories-circle__image"])[7]')
rad_stories_button = (By.XPATH, '(//img[@class="stories-circle__image"])[8]')