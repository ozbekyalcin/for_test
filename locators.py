# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    USERNAME_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginButton")


class SearchLocators(object):
    SEARCH_FIELD = (By.ID, "searchData")
    SEARCH_BUTTON = (By.CLASS_NAME, ".searchBtn")
    SEARCH_RESULT = (By.CLASS_NAME, ".resultText")
    CLOSE_POP_UP = (By.CLASS_NAME, ".seg-popup-close")

class PaginationLocators(object):
    SECOND_PAGE = (By.CSS_SELECTOR, ".pagination a:nth-child(2)")


class ThirdProductLocators(object):
    ADD_FAVORITE_THIRD_PRODUCT = (By.CSS_SELECTOR, "#view > ul > li:nth-child(3) .textImg.followBtn")


class FavoriteProducts(object):
    HOVER_TO_MY_ACCOUNT_MENU = (By.CLASS_NAME, ".myAccount")
    MY_FAVORITE = (By.LINK_TEXT, "İstek Listem / Favorilerim")


class FavoritePageLocators(object):
    GO_TO_FAVORITE_PRODUCT_LIST = (By.CSS_SELECTOR, ".listItemWrap > a > h4")
    DELETE_FAVORITE_PRODUCT = (By.CLASS_NAME, ".deleteProFromFavorites")
    DELETE_FAVORITE_PRODUCT_MESSAGE = (By.CLASS_NAME, ".message")
    CONFIRM_DELETE_FAVORITE_PRODUCT = (By.CSS_SELECTOR, ".btn.btnBlack.confirm")
    EMPTY_FAVORITE_LIST = (By.CSS_SELECTOR, ".emptyWatchList.hiddentext")
