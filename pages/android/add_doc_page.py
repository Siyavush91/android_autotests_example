from selenium.webdriver.common.by import By
from utils.base_page import BasePage

import midhub_constants as mc
import utils.asserts as asserts

class AddDocPage(BasePage):
    back_button           = (By.ID, 'navButton')
    toolbar_title         = (By.ID, 'toolbarTitle')
    search_button         = (By.ID, 'searchButton')
    step_number           = (By.ID, 'stepNumberText')
    list_element_name_id  = "//*[(./@resource-id = 'ru.mobileup.midhub:id/title')]"
    list_element_name     = (By.XPATH, list_element_name_id)
    list_element_price_id = "//*[(./@resource-id = 'ru.mobileup.midhub:id/price')]"
    list_element_price    = (By.XPATH, list_element_price_id)
    subheader             = (By.XPATH, "//*[(./@resource-id = 'ru.mobileup.midhub:id/domainDocumentTemplatesRecyclerView')]/*[(./@class = 'android.widget.TextView')]")

    def page_wait(self):
        self.wait_element_displayed(self.list_element_price) 
        return self


    def verify_page(self):
        self.wait_elements_displayed([self.back_button, self.toolbar_title, self.search_button])
        self.wait_elements_displayed([self.step_number, self.subheader, self.list_element_name, self.list_element_price])
        asserts.soft_assert_equal(self.fetch_elements_name(*self.toolbar_title)[0], mc.CHOOSE_DOC)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.step_number)[0], mc.SECOND_STEP)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.subheader)[0], mc.SUBHEADER)
        return


    def verify_list_element(self, name, value):
        list_element_name_locator = self.locator(self.list_element_name_id, name)
        list_element_price_locator = self.locator(self.list_element_price_id, value)
        self.wait_elements_displayed([list_element_name_locator, list_element_price_locator])
        return self


    def tap_option(self, name):
        list_element_locator = self.locator(self.list_element_name_id, name)
        self.find_tapable_element(*list_element_locator).click()
        return


    def locator(self, raw_id, text):
        xpath = raw_id + f"[contains(@text, '{text}')]"
        return (By.XPATH, xpath)
        