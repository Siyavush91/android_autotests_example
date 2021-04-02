from selenium.webdriver.common.by import By
from utils.base_page import BasePage

import midhub_constants as mc
import utils.asserts as asserts

class VerificationTypePage(BasePage):
    back_button                  = (By.ID, 'navButton')
    toolbar_title                = (By.ID, 'toolbarTitle')
    steps_progress               = (By.ID, 'stepsProgress')
    step_number                  = (By.ID, 'stepNumberText')
    global_verification_title    = (By.ID, 'globalVerificationTitle')
    global_yellow_title          = (By.ID, 'globalYellowVerificationTitle')
    global_yellow_desc           = (By.ID, 'globalYellowVerificationDescription')
    global_yellow_image          = (By.ID, 'globalYellowVerificationImageView')
    global_yellow_choose_button  = (By.ID, 'globalYellowChooseButton')
    global_yellow_details_button = (By.ID, 'globalYellowDetailsButton')
    global_green_title           = (By.ID, 'globalGreenVerificationTitle')
    global_green_desc            = (By.ID, 'globalGreenVerificationDescription')
    global_green_image           = (By.ID, 'globalGreenVerificationImageView')
    global_green_choose_button   = (By.ID, 'globalGreenChooseButton')
    global_green_details_button  = (By.ID, 'globalGreenDetailsButton')
    local_verification_title     = (By.ID, 'localVerificationTitle')
    local_yellow_title           = (By.ID, 'localYellowVerificationTitle')
    local_yellow_desc            = (By.ID, 'localYellowVerificationDescription')
    local_yellow_image           = (By.ID, 'localYellowVerificationImageView')
    local_yellow_choose_button   = (By.ID, 'localYellowChooseButton')
    local_yellow_details_button  = (By.ID, 'localYellowDetailsButton')
    local_green_title            = (By.ID, 'localGreenVerificationTitle')
    local_green_desc             = (By.ID, 'localGreenVerificationDescription')
    local_green_image            = (By.ID, 'localGreenVerificationImageView')
    local_green_choose_button    = (By.ID, 'localGreenChooseButton')
    local_green_details_button   = (By.ID, 'localGreenDetailsButton')
    alert_message                = (By.XPATH, "//*[contains(@resource-id, 'message')]")
    alert_button                 = (By.XPATH, "//*[contains(@resource-id, 'button1')]")

    def page_wait(self):
        self.wait_element_displayed(self.global_verification_title) 
        return self

    def verify_page(self, header):
        self.wait_elements_displayed([self.back_button, self.toolbar_title, self.steps_progress, self.step_number])
        asserts.assert_equal(self.fetch_elements_name(*self.toolbar_title)[0], header)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.step_number)[0], mc.THIRD_STEP)

        self.wait_elements_displayed([self.global_verification_title, self.global_yellow_title, self.global_yellow_desc, self.global_yellow_image, self.global_yellow_choose_button , self.global_yellow_details_button])
        asserts.soft_assert_equal(self.fetch_elements_name(*self.global_verification_title)[0], mc.GLOBAL_VERIFICATION_TITLE)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.global_yellow_title)[0], mc.YELLOW_TITLE)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.global_yellow_desc)[0], mc.GLOBAL_YELLOW_DESC)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.global_yellow_choose_button)[0], mc.VERIFICATION_CHOOSE_BUTTON)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.global_yellow_details_button)[0], mc.VERIFICATION_DETAILS_BUTTON)

        self.scroll_down(self.global_green_choose_button)
        self.wait_elements_displayed([self.global_green_title, self.global_green_desc, self.global_green_image, self.global_green_choose_button , self.global_green_details_button])
        asserts.soft_assert_equal(self.fetch_elements_name(*self.global_green_title)[0], mc.GREEN_TITLE)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.global_green_desc)[0], mc.GLOBAL_GREEN_DESC)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.global_green_choose_button)[0], mc.VERIFICATION_CHOOSE_BUTTON)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.global_green_details_button)[0], mc.VERIFICATION_DETAILS_BUTTON)

        self.scroll_down(self.local_yellow_choose_button)
        self.wait_elements_displayed([self.local_verification_title, self.local_yellow_title, self.local_yellow_desc, self.local_yellow_image, self.local_yellow_choose_button , self.local_yellow_details_button])
        asserts.soft_assert_equal(self.fetch_elements_name(*self.local_verification_title)[0], mc.LOCAL_VERIFICATION_TITLE)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.local_yellow_title)[0], mc.YELLOW_TITLE)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.local_yellow_desc)[0], mc.LOCAL_YELLOW_DESC)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.local_yellow_choose_button)[0], mc.VERIFICATION_CHOOSE_BUTTON)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.local_yellow_details_button)[0], mc.VERIFICATION_DETAILS_BUTTON)

        self.scroll_down(self.local_green_choose_button)
        self.wait_elements_displayed([self.local_green_title, self.local_green_desc, self.local_green_image, self.local_green_choose_button , self.local_green_details_button])
        asserts.soft_assert_equal(self.fetch_elements_name(*self.local_green_title)[0], mc.GREEN_TITLE)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.local_green_desc)[0], mc.LOCAL_GREEN_DESC)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.local_green_choose_button)[0], mc.VERIFICATION_CHOOSE_BUTTON)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.local_green_details_button)[0], mc.VERIFICATION_DETAILS_BUTTON)

        self.scroll_to_global_verification()

    def scroll_to_global_verification(self):
        self.scroll_up(self.global_verification_title)

    def tap_choose_global_green_verification(self):
        self.find_tapable_element(*self.global_green_choose_button).click()

    def tap_choose_global_yellow_verification(self):
        self.find_tapable_element(*self.global_yellow_choose_button).click()

    def tap_details_global_yellow_verification(self):
        self.find_tapable_element(*self.global_yellow_details_button).click()

    def verify_not_supported_verification_alert(self):
        self.wait_elements_displayed([self.alert_message, self.alert_button])
        asserts.soft_assert_equal(self.fetch_elements_name(*self.alert_message)[0], mc.ALERT_NOT_SUPPORTED_VERIF)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.alert_button)[0], mc.ALERT_OK_BUTTON)

    def close_not_supported_verification_alert(self):
        self.find_tapable_element(*self.alert_button).click()