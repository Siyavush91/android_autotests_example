import midhub_constants as mc
import utils.asserts as asserts
import re

from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class WalletInfoPage(BasePage):
    back_button   = (By.ID, 'back')
    address_label = (By.ID, 'walletAddressLabel')
    address_value = (By.ID, 'walletAddress')
    balance_label = (By.ID, 'balanceLabel')
    balance_value = (By.ID, 'balance')
    next_button   = (By.ID, 'next')

    def page_wait(self):
        self.wait_element_displayed(self.address_label)
        return self

    def verify_page(self):
        self.wait_elements_displayed([self.back_button, self.address_label, self.address_value,
                                    self.balance_label, self.balance_value,self.next_button])
        
        asserts.soft_assert_equal(self.fetch_elements_name(*self.address_label)[0], mc.WALLET_INFO_ADDRESS)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.balance_label)[0], mc.WALLET_INFO_BALANCE)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.next_button)[0], mc.WALLET_INFO_NEXT)

        actual_address = self.fetch_elements_name(*self.address_value)[0]
        actual_balance = self.fetch_elements_name(*self.balance_value)[0]
        asserts.assert_is_not_none(re.match('^0x.+$', actual_address))
        asserts.soft_assert_is_not_none(re.match('^[0-9]+ Wei$', actual_balance))
        return

    def tap_next(self):
        self.find_tapable_element(*self.next_button).click()
        return
    