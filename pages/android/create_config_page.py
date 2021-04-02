from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class CreateConfigPage(BasePage):
    create_config_button_raw_id = 'createConfigButton'
    create_config_button        = (By.ID, create_config_button_raw_id)
    name_edit_raw_id            = 'nameEdit'
    url_edit_raw_id             = 'urlEdit'

    def page_wait(self):
        self.wait_element_displayed(self.create_config_button) 
        return self

    def enter_name(self, name):
        self.driver.find_element_by_id(self.name_edit_raw_id).send_keys(name)
        return

    def enter_url(self, url):
        self.driver.find_element_by_id(self.url_edit_raw_id).send_keys(url)
        return
    
    def tap_add(self):
        self.driver.find_element_by_id(self.create_config_button_raw_id).click()
        return