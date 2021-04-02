import re
import sys
import midhub_constants as mc
import utils.asserts as asserts

from time import sleep
from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class TutorialPage(BasePage):
    image        = (By.XPATH, "//*[contains(@resource-id, 'image')][1]")
    title        = (By.XPATH, "//*[contains(@resource-id, 'title')][1]")
    subtitle     = (By.XPATH, "//*[contains(@resource-id, 'subtitle')][1]")
    indicator    = (By.XPATH, "//*[contains(@resource-id, 'indicator')][1]")
    close_button = (By.XPATH, "//*[contains(@resource-id, 'close')][1]")
    next_button  = (By.XPATH, "//*[contains(@resource-id, 'next')][1]")

    def page_wait(self):
        self.wait_element_displayed(self.next_button)
        return self

    def verify_page(self, number_of_page):
        self.wait_elements_displayed([self.image, self.title, self.subtitle, self.indicator, self.next_button,self.close_button]) 
        self.check_lexemes(number_of_page)
        return

    def tap_next_button(self):
        self.find_tapable_element(*self.next_button).click()
        return

    def tap_close_button(self):
        self.find_tapable_element(*self.close_button).click()
        return

    def check_lexemes(self, number_of_page, only_title = False):
        if number_of_page == 1:
            expected_title = mc.TUTORIAL_PAGE1_TITLE
            expected_subtitle = mc.TUTORIAL_PAGE1_SUBTITLE
        elif number_of_page == 2:
            expected_title = mc.TUTORIAL_PAGE2_TITLE
            expected_subtitle = mc.TUTORIAL_PAGE2_SUBTITLE
        elif number_of_page == 3:
            expected_title = mc.TUTORIAL_PAGE3_TITLE
            expected_subtitle = mc.TUTORIAL_PAGE3_SUBTITLE
        else:
            raise 'Unsupported number of page for tutorial'

        asserts.soft_assert_equal(self.fetch_elements_name(*self.title)[0], expected_title)
        if only_title == False:
            asserts.soft_assert_equal(self.fetch_elements_name(*self.subtitle)[0], expected_subtitle)
        return
