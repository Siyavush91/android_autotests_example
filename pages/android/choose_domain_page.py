from selenium.webdriver.common.by import By
from utils.base_page import BasePage

import midhub_constants as mc
import utils.asserts as asserts

class ChooseDomainPage(BasePage):
    back_button         = (By.ID, 'navButton')
    toolbar_title       = (By.ID, 'toolbarTitle')
    search_button       = (By.ID, 'searchButton')
    clear_search_btn    = (By.ID, 'clearButton')
    search_field_by_id  = 'searchEditText'
    step_number         = (By.ID, 'stepNumberText')
    country_group_title = (By.ID, 'countryGroupTitle')
    flag                = (By.ID, 'flag')
    # list_element_id     = "//*[(./@resource-id = 'ru.mobileup.midhub:id/countriesRecyclerView')]/*[(./@resource-id = 'ru.mobileup.midhub:id/title')]"
    # list_element        = (By.XPATH, list_element_id)
    list_element_id     = "//*[(./@resource-id = 'ru.mobileup.midhub:id/title')]"
    list_element        = (By.ID, 'title')

    def page_wait(self):
        self.wait_element_displayed(self.list_element)
        return self

    def verify_header(self):
        self.wait_elements_displayed([self.back_button, self.toolbar_title, self.search_button])
        asserts.soft_assert_equal(self.fetch_elements_name(*self.toolbar_title)[0], mc.ENTER_NAME)
        return

    def verify_page(self):
        self.wait_elements_displayed([self.back_button, self.toolbar_title, self.search_button])
        self.wait_elements_displayed([self.step_number, self.country_group_title, self.flag, self.list_element])
        asserts.soft_assert_equal(self.fetch_elements_name(*self.step_number)[0], mc.FIRST_STEP)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.country_group_title)[0], mc.COUNTRY_GROUP_TITLE)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.toolbar_title)[0], mc.CHOOSE_COUNTRY_HEADER)
        return


    def tap_domain(self, name):
        domain_locator = self.locator(name)
        self.find_tapable_element(*domain_locator).click()
        return


    def locator(self, text):
        xpath = self.list_element_id + f"[contains(@text, '{text}')]"
        return (By.XPATH, xpath)


    def tap_search_btn(self):
        self.find_tapable_element(*self.search_button).click()

    def tap_clear_search_btn(self):
        self.find_tapable_element(*self.clear_search_btn).click()

    def verify_keyboard(self):
        asserts.assert_true(self.driver.is_keyboard_shown(), 'Keyboard is not shown')

    def enter_search(self, value):
        self.driver.find_element_by_id(self.search_field_by_id).send_keys(value)
        return

    def scroll_down_to_domain(self):
        self.scroll_down(self.list_element)

    def verify_domain(self, value):
        self.wait_elements_displayed([self.flag, self.list_element])
        asserts.soft_assert_equal(self.fetch_elements_name(*self.list_element)[0], value)
        return

    #need refactor after add msg on screen
    def verify_not_found_msg(self):
        self.wait_element_displayed(self.step_number)
        return self

