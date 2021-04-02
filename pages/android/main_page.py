from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class MainPage(BasePage):
    menu_bottom_main   = (By.ID, 'menuButtonMain')
    menu_bottom_wallet = (By.ID, 'menuButtonWallet')
    menu_bottom_docs   = (By.ID, 'menuButtonAccountDocuments')
    tab_title          = (By.ID, 'tabTitle')

    def page_wait(self):
        self.wait_element_displayed(self.tab_title) 
        return self

    def tap_wallet_tab(self):
        self.find_tapable_element(*self.menu_bottom_wallet).click()
        return

    def tap_docs_tab(self):
        self.find_tapable_element(*self.menu_bottom_docs).click()
        return