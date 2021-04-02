from selenium.webdriver.common.by import By
from utils.base_page import BasePage

import midhub_constants as mc
import utils.asserts as asserts
import re

class FieldPage(BasePage):
    back_button           = (By.ID, 'back')
    confirm_button        = (By.ID, 'confirm')
    progress_label        = (By.ID, 'progressLabel')
    progress_scale        = (By.ID, 'progressScale')
    progress_current_step = (By.ID, 'progressCurrentStep')
    previous_button       = (By.ID, 'previous') 
    next_button           = (By.ID, 'next')
    ready_button          = (By.ID, 'ready')
    text_field            = (By.ID, 'textInputLayout')
    edit_text_raw_id      = 'editText'
    edit_field            = (By.ID, edit_text_raw_id)
    field_checkbox        = (By.ID, 'textView')
    date_hint             = (By.ID, 'hint')
    mask_hint             = (By.ID, 'formatHint')

    def page_wait(self):
        self.wait_elements_displayed([self.back_button, self.confirm_button]) 
        return self

    def verify_step_screen(self, expected_current_step, expected_overall_steps):
        if self.driver.is_keyboard_shown():
            self.tap_device_back()
        self.wait_elements_displayed([self.progress_label, self.progress_scale, self.progress_current_step, self.previous_button])
        asserts.assert_true(self.element_exists(self.next_button) or self.element_exists(self.ready_button), 'Next or Ready button should be displayed')
        actual_current_step = re.search('^Шаг ([0-9]+) из [0-9]+$', self.fetch_elements_name(*self.progress_label)[0]).group(1)
        actual_overall = re.search('^Шаг [0-9]+ из ([0-9]+)$', self.fetch_elements_name(*self.progress_label)[0]).group(1)
        asserts.assert_equal(actual_current_step, str(expected_current_step))
        asserts.assert_equal(actual_overall, str(expected_overall_steps))

    def verify_content(self, field_type, field_name):
        if field_type == 'Text' or field_type == 'Number':
            self.verify_text_form(field_name)
        elif field_type == 'Date':
            self.verify_date_form(field_name)
        elif field_type == 'Checkbox':
            self.verify_checkbox_form(field_name)
        else:
            raise NotImplementedError('Not supported field type')

    def verify_mask_hint(self, mask):
        asserts.assert_equal(self.fetch_elements_name(*self.mask_hint)[0], mask)

    def tap_next_button(self):
        self.find_tapable_element(*self.next_button).click()
    
    def tap_ready_button(self):
        self.find_tapable_element(*self.ready_button).click()

    def tap_confirm_button(self):
        self.find_tapable_element(*self.confirm_button).click()

    def tap_previous_step_button(self):
        self.find_element(*self.previous_button).click()

    def tap_back_button(self):
        self.find_tapable_element(*self.back_button).click()

    def last_step(self):
        actual_current_step = re.search('^Шаг ([0-9]+) из [0-9]+$', self.fetch_elements_name(*self.progress_label)[0]).group(1)
        actual_overall = re.search('^Шаг [0-9]+ из ([0-9]+)$', self.fetch_elements_name(*self.progress_label)[0]).group(1)
        return actual_current_step == actual_overall

    def fill_field(self, field_type, value, mask = False):
        if field_type == 'Text' or field_type == 'Number':
            if not self.driver.is_keyboard_shown():
                self.tap_text_field()
            self.fill_text_field(value, mask)
            self.tap_next_keyboard()
        elif field_type == 'Date':
            if not self.driver.is_keyboard_shown():
                self.tap_text_field()
            self.fill_date_field(value)
            self.tap_next_keyboard()
        elif field_type == 'Checkbox':
            self.fill_checkbox_field(value)
        else:
            raise NotImplementedError('Not supported field type')

    def verify_text_form(self, field_name, check_keyboard = True):
        self.wait_elements_displayed([self.text_field, self.edit_field])
        asserts.assert_equal(self.fetch_elements_name(*self.edit_field)[0], field_name)
        if check_keyboard:
            asserts.assert_true(self.driver.is_keyboard_shown(), 'Keyboard is not shown')

    def tap_text_field(self):
        self.find_tapable_element(*self.edit_field).click()

    def fill_text_field(self, value, mask = False):
        self.driver.find_element_by_id(self.edit_text_raw_id).send_keys(value)
        if mask:
            asserts.assert_equal(self.fetch_elements_name(*self.edit_field)[0], mask)

    def verify_checkbox_form(self, field_name):
        self.wait_element_displayed(self.field_checkbox)
        asserts.assert_equal(self.fetch_elements_name(*self.field_checkbox)[0], field_name)
        asserts.assert_false(self.driver.is_keyboard_shown(), 'Keyboard is shown')
        
    def fill_checkbox_field(self, value):
        locator = self.locator(value)
        self.find_tapable_element(*locator).click()
    
    def locator(self, text):
        xpath = f"//*[contains(@text, '{text}')]"
        return (By.XPATH, xpath)

    def verify_date_form(self, field_name, check_keyboard = True):
        self.verify_text_form(field_name, check_keyboard)
        self.wait_element_displayed(self.date_hint)
        asserts.assert_equal(self.fetch_elements_name(*self.date_hint)[0], 'DD.MM.YYYY')

    def fill_date_field(self, value):
        self.driver.find_element_by_id(self.edit_text_raw_id).send_keys(value)

    def clean_field(self):
        self.driver.find_element_by_id(self.edit_text_raw_id).clear()