from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class TopUpInfoPage(BasePage):
    qr_code     = (By.ID, 'qrCode')
    copy_button = (By.ID, 'copyWalletAddressButton')

    def page_wait(self):
        self.wait_element_displayed(self.qr_code) 
        return self

    def tap_copy(self):
        self.find_tapable_element(*self.copy_button).click()
        return