#!/usr/bin/env python
# -*- coding: utf-8 -*-
from nonbir.n11 import *


class NOnBirTestCases(unittest.TestCase, MainPageControls, LoginPageControls, SearchDataControls, SecondPageControls,
                      FavoriteProductControls, FavoritePageControls, DeleteFavoriteList):

    def setUp(self):
        MainPageControls.__init__(self)

    def test_n11_website(self):
        self.go_to_homepage_and_comfirm_homepage()
        main_page_title = "n11.com - Alışverişin Uğurlu Adresi"
        self.assertEqual(main_page_title, self.driver.title.encode('utf8'))
        self.user_login_in_to_the_website()
        username_control = "yalcinozbek"
        self.assertEqual(username_control, self.driver.execute_script(
            "return $('.myAccount').text().replace(/\s/g,'').replace('Hesabım','')"))
        self.search_data_and_confirm_data_exist()
        result_text = "sonuçbulundu."
        self.assertIn(result_text, self.driver.execute_script("return $('.resultText').text().replace(/\s/g,'')")
                      .encode('utf8'))
        self.go_to_second_page_and_confirm_second_page_exist()
        self.assertIn('pg=2', self.driver.current_url, 'Page change failed.')
        self.click_add_product_in_favorite()
        self.click_my_favorite()
        self.assertIn("https://", self.driver.execute_script("return $('.listItemProductList > li > a').attr('href')"))
        self.delete_product_in_favorite()
        empty_favorite_list_text = self.get_wait().until(
            ec.element_to_be_clickable(FavoritePageLocators.EMPTY_FAVORITE_LIST)).text
        self.assertEqual("İzlediğiniz bir ürün bulunmamaktadır.", empty_favorite_list_text.encode('utf-8'))

    def tearDown(self):
        self.driver.close()
