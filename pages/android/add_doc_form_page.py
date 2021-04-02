from selenium.webdriver.common.by import By
from utils.base_page import BasePage
from time import sleep

import midhub_constants as mc
import utils.asserts as asserts

class AddDocFormPage(BasePage):
    back_button            = (By.ID, 'navButton')
    toolbar_title          = (By.ID, 'toolbarTitle')
    steps_progress         = (By.ID, 'stepsProgress')
    step_number            = (By.ID, 'stepNumberText')
    text_input_container   = (By.ID, 'textInputLayout')
    edit_text_field_id     = "//*[(./@resource-id = 'ru.mobileup.midhub:id/editText')]"
    edit_text_field        = (By.ID, 'editText')
    next_button            = (By.ID, 'nextButton')
    scroll_view            = (By.ID, 'scrollView')
    agreement_label        = (By.ID, 'agreementLabel')
    agreement_switch       = (By.ID, 'agreementSwitch')
    progress_bar_container = (By.ID, 'progressContainer')
    # Photo locators
    header                 = (By.ID, 'label')
    add_photo_button       = (By.ID, 'addPhoto')
    hint                   = (By.ID, 'hint')
    photo                  = (By.ID, 'photo')
    remove_photo           = (By.ID, 'remove')
    warning                = (By.ID, 'error')
    warning_text           = (By.ID, 'textinput_error')

    def page_wait(self):
        asserts.assert_equal(self.fetch_elements_name(*self.toolbar_title)[0], mc.ADD_DOC_FORM_HEADER)
        return self

    def verify_page(self, page_type, add_photo_button_state):
        self.wait_elements_displayed([self.back_button, self.toolbar_title, self.steps_progress, self.step_number])
        asserts.assert_equal(self.fetch_elements_name(*self.toolbar_title)[0], mc.ADD_DOC_FORM_HEADER)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.step_number)[0], mc.FOURTH_STEP)
        
        # if current_page == '1':
        #     for x in range(0, int(overall)):
        #         asserts.assert_equal(int(self.fetch_elements_name(*self.step_number)[x]), x+1)
        # elif current_page != overall:
        #     asserts.assert_equal(int(self.fetch_elements_name(*self.step_number)[0]), int(current_page))
        #     asserts.assert_equal(int(self.fetch_elements_name(*self.step_number)[1]), int(current_page)+1)
        # elif current_page == overall:
        #     asserts.assert_equal(int(self.fetch_elements_name(*self.step_number)[0]), int(current_page))
        #     self.scroll_to_the_bottom()
        #     self.verify_agreement()
        # else:
        #     raise('Incorrect value for page!')
        self.scroll_to_the_bottom()
        self.verify_next_button()
        self.scroll_to_the_top()
        if page_type == 'Text':
            self.verify_text_page_type()
        elif page_type == 'Photo':
            if add_photo_button_state == None or add_photo_button_state == 'True':
                add_photo_button_state = True
            elif add_photo_button_state == 'False':
                add_photo_button_state = False
            else:
                raise('Unsupported type of value for add_photo')
            self.verify_photo_page_type(add_photo_button_state)
        return

    def verify_agreement(self):
        self.wait_elements_displayed([self.agreement_label, self.agreement_switch])
        asserts.soft_assert_equal(self.fetch_elements_name(*self.agreement_label)[0], mc.AGREEMENT_LABEL)
        return

    def verify_next_button(self):
        self.wait_element_displayed(self.next_button)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.next_button)[0], mc.NEXT_BUTTON)
        return

    def verify_text_page_type(self):
        self.wait_elements_displayed([self.text_input_container, self.edit_text_field])
        return

    def verify_photo_page_type(self, add_photo_button_state):
        checked_element = self.add_photo_button if add_photo_button_state else self.photo
        self.wait_elements_displayed([self.header, checked_element])
        return

    def verify_photo_page_header_lexeme(self, lexeme):
        self.wait_element_displayed(self.header)
        asserts.assert_equal(self.fetch_elements_name(*self.header)[0], lexeme)
        return

    def verify_photo_hint(self, value):
        self.wait_element_displayed(self.hint)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.hint)[0], value)
        return

    def verify_field(self, name):
        texts = self.fetch_elements_name(*self.edit_text_field)
        asserts.assert_in(name, texts.values())
        return

    def verify_warning_for_field(self, field, warning):
        loc = "//*[contains(@text, '" + field + "')]/parent::*/parent::*[(./@resource-id = 'ru.mobileup.midhub:id/textInputLayout')]/*/*/*[(./@resource-id = 'ru.mobileup.midhub:id/textinput_error')][contains(@text, '" + warning + "')]"
        warning_locator = (By.XPATH, loc)
        self.wait_element_displayed(warning_locator)
        return

    def verify_warning_for_fields(self, number, warning):
        loc = "//*[(./@resource-id = 'ru.mobileup.midhub:id/textInputLayout')]/*/*/*[(./@resource-id = 'ru.mobileup.midhub:id/textinput_error')][contains(@text, '" + warning + "')]"
        warning_locator = (By.XPATH, loc)
        self.wait_element_displayed(warning_locator)
        asserts.assert_equal(len(self.fetch_elements_name(*warning_locator)), int(number))
        return

    def verify_no_warning_for_field(self, field):
        loc = "//*[contains(@text, '" + field + "')]/parent::*/parent::*[(./@resource-id = 'ru.mobileup.midhub:id/textInputLayout')]/*/*/*[(./@resource-id = 'ru.mobileup.midhub:id/textinput_error')]"
        warning_locator = (By.XPATH, loc)
        asserts.assert_false(self.is_element_found(warning_locator), "Warning is present, but shouldn't be")
        return

    def verify_no_warning_for_all_fields(self):
        asserts.assert_false(self.is_element_found(self.warning_text), "Warning is present, but shouldn't be")
        return

    def next_button_exists(self):
        return self.is_element_found(self.next_button)

    def field_displayed(self, text):
        self.element_exists(self.edit_text_field, text=text)

    def check_attached_photo(self, number):
        self.wait_elements_displayed([self.photo, self.remove_photo])
        asserts.assert_equal(len(self.find_elements(*self.remove_photo)), int(number))

    def verify_photo_warning(self, warning):
        self.wait_element_displayed(self.warning)
        asserts.soft_assert_equal(self.fetch_elements_name(*self.warning)[0], warning)

    def tap_next_button(self):
        self.scroll_down(self.next_button)
        self.find_tapable_element(*self.next_button).click()

    def tap_field(self, name):
        field_locator = self.locator(name)
        self.find_tapable_element(*field_locator).click()

    def tap_first_field(self):
        self.find_tapable_element(*self.edit_text_field).click()

    def tap_add_photo_button(self):
        self.find_tapable_element(*self.add_photo_button).click()

    def tap_back(self):
        self.find_tapable_element(*self.back_button).click()

    def tap_agreement_switch(self):
        self.find_tapable_element(*self.agreement_switch).click()

    def tap_on_agreement_link(self):
        self.find_tapable_element(*self.agreement_label).click()

    def scroll_to_the_bottom(self):
        self.scroll_down(self.next_button)

    def scroll_to_the_top(self):
        self.scroll_to_top_of_view(self.scroll_view)

    def scroll_down_to_field(self, text):
        self.scroll_down(self.edit_text_field, text=text)

    def locator(self, text):
        xpath = self.edit_text_field_id + f"[contains(@text, '{text}')]"
        return (By.XPATH, xpath)

    def wait_loader_not_displayed(self):
        self.wait_element_not_displayed(self.progress_bar_container)
        sleep(0.5)
        self.wait_element_not_displayed(self.progress_bar_container)