# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    USERNAME_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginButton")


class SearchLocators(object):
    SEARCH_FIELD = (By.ID, "searchData")
    SEARCH_BUTTON = (By.CLASS_NAME, "searchBtn")
    SEARCH_RESULT = (By.CLASS_NAME, "resultText")


class PaginationLocators(object):
    SECOND_PAGE = (By.CSS_SELECTOR, ".pagination a:nth-child(2)")
