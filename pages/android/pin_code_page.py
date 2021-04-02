import logging
import re
import sys
import midhub_constants as mc
import utils.asserts as asserts

from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class PinCodePage(BasePage):
    pin_code_edit        = (By.XPATH, "//*[contains(@resource-id, 'pinCodeEdit')]")
    login_button         = (By.XPATH, "//*[contains(@resource-id, 'createAccount')]")
    back_button          = (By.XPATH, "//*[contains(@resource-id, 'back')]")
    login_button_raw_id  = 'createAccount'
    pin_code_edit_raw_id = 'pinCodeEdit'

    def page_wait(self):
        self.wait_element_displayed(self.pin_code_edit) 
        return self

    def verify_page(self):
        self.wait_elements_displayed([self.back_button, self.login_button, self.pin_code_edit])
        asserts.assert_false(self.login_button_tappable(), 'Login button is tappable, but should not be')
        asserts.assert_true(self.driver.is_keyboard_shown(), 'Keyboard is not shown')
        asserts.soft_assert_equal(self.fetch_elements_name(*self.login_button)[0], mc.LOGIN_BUTTON)
        return

    def login_button_tappable(self):
        return self.is_element_enabled(self.login_button_raw_id)

    def tap_login(self):
        self.find_tapable_element(*self.login_button).click()
        return

    def enter_pin_code(self, pin):
        self.driver.find_element_by_id(self.pin_code_edit_raw_id).send_keys(pin)
        return
