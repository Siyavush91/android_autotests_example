from selenium.webdriver.common.by import By
from utils.base_page import BasePage

import midhub_constants as mc
import utils.asserts as asserts
import re

class RequestInProgress(BasePage):
    back_button          = (By.ID, 'back')
    message              = (By.ID, 'message')
    notification_message = (By.ID, 'notificationMessage')
    application_status   = (By.ID, 'applicationStatus')

    def page_wait(self):
        self.wait_element_displayed(self.message) 
        return self

    def verify_page(self):
        self.wait_elements_displayed([self.back_button, self.message, self.notification_message])
        asserts.soft_assert_equal(self.fetch_elements_name(*self.message)[0], mc.REQUEST_MESSAGE)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.notification_message)[0], mc.NOTIFICATION_MESSAGE)
        asserts.assert_is_not_none(re.match('^.+Status: CREATED$', self.fetch_elements_name(*self.application_status, timer=180)[0]))
        return

    def tap_back(self):
        self.find_tapable_element(*self.back_button).click()