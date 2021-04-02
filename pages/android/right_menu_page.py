from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class RightMenuPage(BasePage):
    config_button = (By.XPATH, "//*[contains(@text, 'CONFIGS')]")
    menu          = (By.ID, 'dd_actions_title')

    def page_wait(self):
        self.wait_element_displayed(self.menu) 
        return self

    def right_menu_opened(self):
        return self.is_element_found(self.menu) 

    def tap_config(self):
        self.find_tapable_element(*self.config_button).click()
        return