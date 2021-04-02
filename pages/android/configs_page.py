from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class ConfigsPage(BasePage):
    stage      = (By.XPATH, "//*[contains(@text, 'Stage')]")
    add_button = (By.ID, 'addConfigButton')

    def page_wait(self):
        self.wait_element_displayed(self.stage) 
        return self

    def tap_stage(self):
        self.find_tapable_element(*self.stage).click()
        return

    def tap_add(self):
        self.find_tapable_element(*self.add_button).click()
        return

    def tap_config(self, name):
        config_locator = self.locator(name)
        self.find_tapable_element(*config_locator).click()
        return
    
    def locator(self, text):
        xpath = f"//*[contains(@text, '{text}')]"
        return (By.XPATH, xpath)

    def config_exists(self, name):
        config_locator = self.locator(name)
        return self.is_element_found(config_locator)
