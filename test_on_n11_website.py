#!/usr/bin/env python
# -*- coding: utf-8 -*-
from modules import *


class Test(unittest.TestCase):
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

    def setUp(self):
        driver_path = os.path.join(os.getcwd(), 'chromedriverLinux64')
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(driver_path, chrome_options=chrome_options)
        self.__wait = WebDriverWait(self.driver, 20)

    def test_go_to_homepage_and_comfirm_homepage(self):
        self.driver.get("https://www.n11.com/")
        main_page_title = "n11.com - Alışverişin Uğurlu Adresi"
        self.assertEqual(main_page_title, self.driver.title.encode('utf8'))

    def test_user_login_in_to_the_website(self):
        self.driver.get("https://www.n11.com/giris-yap")
        email = "yalcinozbek0@gmail.com"
        password = "keytorc123"
        username_control = "yalcinozbek"
        self.get_wait().until(ec.element_to_be_clickable(LoginPageLocators.USERNAME_FIELD)).send_keys(email)
        self.get_wait().until(ec.element_to_be_clickable(LoginPageLocators.PASSWORD_FIELD)).send_keys(password)
        self.click(LoginPageLocators.LOGIN_BUTTON)
        self.assertEqual(username_control, self.driver.execute_script(
            "return $('.myAccount').text().replace(/\s/g,'').replace('Hesabım','')"))

    def test_search_data_and_confirm_data_exist(self):
        self.test_user_login_in_to_the_website()
        self.click(SearchLocators.SEARCH_FIELD)
        self.get_wait().until(ec.element_to_be_clickable(SearchLocators.SEARCH_FIELD)).send_keys("samsung")
        self.click(SearchLocators.CLOSE_POP_UP)
        self.click(SearchLocators.SEARCH_BUTTON)
        result_text = "sonuçbulundu."
        self.assertIn(result_text, self.driver.execute_script("return $('.resultText').text().replace(/\s/g,'')")
                      .encode('utf8'))

    def test_go_to_second_page_and_confirm_second_page_exist(self):
        self.test_search_data_and_confirm_data_exist()
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(2)
        self.click(PaginationLocators.SECOND_PAGE)
        current_page_url = self.driver.current_url
        self.assertIn('pg=2', current_page_url, 'Page change failed.')

    def test_click_add_product_in_favorite(self):
        self.test_go_to_second_page_and_confirm_second_page_exist()
        self.driver.execute_script("window.scrollBy(0,1400)")
        time.sleep(2)
        self.click(ThirdProductLocators.ADD_FAVORITE_THIRD_PRODUCT)

    def test_click_my_favorite(self):
        self.test_click_add_product_in_favorite()
        self.driver.execute_script('window.scrollTo(0, 0)')
        hover_to_menu = self.driver.find_element_by_class_name('myAccount')
        ActionChains(self.driver).move_to_element(hover_to_menu).perform()
        self.click(FavoriteProducts.MY_FAVORITE)

    def test_check_favorite_list(self):
        self.test_click_my_favorite()
        product_url_in_favorite_list = self.driver.execute_script(
            "return $('.listItemProductList > li > a').attr('href')")
        self.assertIn("https://", product_url_in_favorite_list)

    def test_delete_product_in_favorite(self):
        self.test_check_favorite_list()
        self.click(FavoritePageLocators.GO_TO_FAVORITE_PRODUCT_LIST)
        self.click(FavoritePageLocators.DELETE_FAVORITE_PRODUCT)
        self.click(FavoritePageLocators.CONFIRM_DELETE_FAVORITE_PRODUCT)
        empty_favorite_list_text = self.get_wait().until(
            ec.element_to_be_clickable(FavoritePageLocators.EMPTY_FAVORITE_LIST)).text
        self.assertEqual("İzlediğiniz bir ürün bulunmamaktadır.", empty_favorite_list_text.encode('utf-8'))

    def tearDown(self):
        self.driver.quit()
