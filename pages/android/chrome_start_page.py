from selenium.webdriver.common.by import By
from utils.base_page import BasePage
from time import sleep

import utils.asserts as asserts

class ChromeStartPage(BasePage):
    accept_button    = (By.XPATH, "//*[(./@resource-id = 'com.android.chrome:id/terms_accept')]")
    no_thanks_button = (By.XPATH, "//*[(./@resource-id = 'com.android.chrome:id/negative_button')]")

    def accept_button_exists(self):
        sleep(1)
        return self.is_element_found(self.accept_button)

    def tap_accept_button(self):
        self.find_tapable_element(*self.accept_button).click()
        sleep(1)

    def tap_no_thanks(self):
        self.find_tapable_element(*self.no_thanks_button).click()