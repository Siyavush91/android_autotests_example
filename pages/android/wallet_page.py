from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class WalletPage(BasePage):
    balance       = (By.ID, 'balance')
    top_up_button = (By.ID, 'topUpFunds')

    def page_wait(self):
        self.wait_element_displayed(self.balance) 
        return self

    def tap_top_up(self):
        self.find_tapable_element(*self.top_up_button).click()
        return