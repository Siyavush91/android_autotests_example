from selenium.webdriver.common.by import By
from utils.base_page import BasePage

import midhub_constants as mc
import utils.asserts as asserts

class VerificationDetailsPage(BasePage):
    back_button      = (By.ID, 'backButton')
    background_image = (By.ID, 'backgroundImage')
    title            = (By.ID, 'verificationDetailsTitle')
    subtitle         = (By.ID, 'verificationDetailsSubtitle')
    description      = (By.ID, 'verificationDetailsDescription')
    card_image       = (By.ID, 'cardImageView')
    point_one_icon   = (By.ID, 'pointOneIcon')
    point_one_text   = (By.ID, 'pointOneText')
    point_two_icon   = (By.ID, 'pointTwoIcon')
    point_two_text   = (By.ID, 'pointTwoText')
    point_three_icon = (By.ID, 'pointThreeIcon')
    point_three_text = (By.ID, 'pointThreeText')
    point_four_icon  = (By.ID, 'pointFourIcon')
    point_four_text  = (By.ID, 'pointFourText')
    choose_button    = (By.ID, 'verificationDetailsChooseButton')

    def page_wait(self):
        self.wait_element_displayed(self.title) 
        return self

    def verify_page(self):
        # TODO: ваш универсальный ключ lexeme is not covered, there is no id for this element
        self.wait_elements_displayed([self.back_button, self.background_image, self.title, self.subtitle, self.description, self.card_image, self.choose_button])
        self.wait_elements_displayed([self.point_one_icon, self.point_one_text, self.point_two_icon, self.point_two_text, self.point_three_icon, self.point_three_text, self.point_four_icon, self.point_four_text])
        asserts.soft_assert_equal(self.fetch_elements_name(*self.title)[0], mc.YELLOW_MAIN_TITLE)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.subtitle)[0], mc.YELLOW_SUBTITLE)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.description)[0], mc.YELLOW_DESC)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.point_one_text)[0], mc.YELLOW_POINT_ONE)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.point_two_text)[0], mc.YELLOW_POINT_TWO)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.point_three_text)[0], mc.YELLOW_POINT_THREE)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.point_four_text)[0], mc.YELLOW_POINT_FOUR)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.choose_button)[0], mc.VERIFICATION_CHOOSE_BUTTON)

    def tap_choose_button(self):
        self.find_tapable_element(*self.choose_button).click()

    def tap_back_button(self):
        self.find_tapable_element(*self.back_button).click()