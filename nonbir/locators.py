# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    USERNAME_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginButton")


class SearchLocators(object):
    SEARCH_FIELD = (By.ID, "searchData")
    SEARCH_BUTTON = (By.CLASS_NAME, ".searchBtn")


class PaginationLocators(object):
    SECOND_PAGE = (By.CSS_SELECTOR, ".pagination a:nth-child(2)")


class FavoriteProducts(object):
    MY_FAVORITE = (By.LINK_TEXT, "İstek Listem / Favorilerim")


class FavoritePageLocators(object):
    GO_TO_FAVORITE_PRODUCT_LIST = (By.CSS_SELECTOR, ".listItemWrap > a > h4")
    CONFIRM_DELETE_FAVORITE_PRODUCT = (By.CSS_SELECTOR, ".btn.btnBlack.confirm")
    EMPTY_FAVORITE_LIST = (By.CSS_SELECTOR, ".emptyWatchList.hiddentext")
