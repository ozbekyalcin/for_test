#!/usr/bin/env python
# -*- coding: utf-8 -*-
from modules import *


class Configuration(object):

    def __init__(self):
        driver_path = os.path.join(os.getcwd(), 'nonbir/driver/chromedriverLinux64')
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(driver_path, chrome_options=chrome_options)
        self.__wait = WebDriverWait(self.driver, 20)

    def get_wait(self, timeout=20):
        self.__wait._timeout = timeout
        return self.__wait

    def click(self, css_selector):
        try:
            self.get_wait(timeout=10).until(ec.element_to_be_clickable(css_selector)).click()
        except (StandardError, WebDriverException):
            try:
                css_selector = '{}'.format(css_selector[1])
                self.driver.execute_script("var css_selector = document.querySelector("
                                           "'{css_selector}');css_selector.scrollIntoView()"
                                           .format(css_selector=css_selector))
                find_locator = self.get_wait(timeout=5).until(
                    ec.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
                find_locator.click()
            except (StandardError, WebDriverException):
                raise


class MainPageControls(Configuration):
    def go_to_homepage_and_comfirm_homepage(self):
        self.driver.get("https://www.n11.com/")


class LoginPageControls(Configuration):
    def user_login_in_to_the_website(self):
        self.driver.get("https://www.n11.com/giris-yap")
        email = "yalcinozbek0@gmail.com"
        password = "keytorc123"
        self.get_wait().until(ec.element_to_be_clickable(LoginPageLocators.USERNAME_FIELD)).send_keys(email)
        self.get_wait().until(ec.element_to_be_clickable(LoginPageLocators.PASSWORD_FIELD)).send_keys(password)
        self.click(LoginPageLocators.LOGIN_BUTTON)


class SearchDataControls(Configuration):
    def search_data_and_confirm_data_exist(self):
        self.get_wait().until(ec.element_to_be_clickable(SearchLocators.SEARCH_FIELD)).send_keys("samsung")
        self.click(SearchLocators.SEARCH_BUTTON)


class SecondPageControls(Configuration):
    def go_to_second_page_and_confirm_second_page_exist(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.click(PaginationLocators.SECOND_PAGE)


class FavoriteProductControls(Configuration):
    def click_add_product_in_favorite(self):
        self.driver.execute_script("window.scrollBy(0,800)")
        time.sleep(2)
        self.driver.execute_script("$('div[data-position=31] .followBtn')[0].click()")


class FavoritePageControls(Configuration):
    def click_my_favorite(self):
        self.driver.execute_script("window.scrollTo(0, 0)")
        hover_to_menu = self.driver.find_element_by_class_name('myAccount')
        ActionChains(self.driver).move_to_element(hover_to_menu).perform()
        self.click(FavoriteProducts.MY_FAVORITE)


class DeleteFavoriteList(Configuration):
    def delete_product_in_favorite(self):
        self.click(FavoritePageLocators.GO_TO_FAVORITE_PRODUCT_LIST)
        self.driver.execute_script("$('.deleteProFromFavorites').click()")
        self.click(FavoritePageLocators.CONFIRM_DELETE_FAVORITE_PRODUCT)
