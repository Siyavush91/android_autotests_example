import re
import sys
import midhub_constants as mc
import utils.asserts as asserts

from time import sleep
from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class StartPage(BasePage):
    login_button      = (By.XPATH, "//*[contains(@resource-id, 'login')]")
    create_acc_button = (By.XPATH, "//*[contains(@resource-id, 'createAccount')]")
    text_view         = (By.XPATH, "//android.widget.TextView")

    def page_wait(self):
        self.wait_element_displayed(self.login_button) 
        return self

    def verify_page(self):
        self.wait_elements_displayed([self.login_button, self.create_acc_button, self.text_view]) 
        actual_login = self.fetch_elements_name(*self.login_button)[0]
        actual_create = self.fetch_elements_name(*self.create_acc_button)[0]
        texts = self.fetch_elements_name(*self.text_view)
        asserts.soft_assert_equal(actual_login, mc.LOGIN_BUTTON)
        asserts.soft_assert_equal(actual_create, mc.CREATE_ACC_BUTTON)
        asserts.soft_assert_in(mc.LOGO, texts.values())
        asserts.soft_assert_in(mc.SUBTITLE_LOGIN, texts.values())
        return

    def tap_create_acc(self):
        self.find_tapable_element(*self.create_acc_button).click()
        return
