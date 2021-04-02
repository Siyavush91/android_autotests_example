from selenium.webdriver.common.by import By
from utils.base_page import BasePage
from time import sleep

class PermissionAlert(BasePage):
    allow_button        = (By.XPATH, "//*[contains(@resource-id, 'permission_allow_button')]")
    always_allow_button = (By.XPATH, "//*[contains(@resource-id, 'permission_allow_always_button')]")

    def page_wait(self):
        self.wait_element_displayed(self.allow_button) 
        return self

    def tap_allow(self):
        if self.is_element_found(self.allow_button):
            self.find_tapable_element(*self.allow_button).click()
        elif self.is_element_found(self.always_allow_button):
            self.find_tapable_element(*self.always_allow_button).click()
        return

    def permission_exists(self):
        sleep(1)
        return self.is_element_found(self.allow_button) or self.is_element_found(self.always_allow_button)