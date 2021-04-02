from selenium.webdriver.common.by import By
from utils.base_page import BasePage
from time import sleep

import midhub_constants as mc
import utils.asserts as asserts

class CameraPage(BasePage):
    shutter_button = (By.XPATH, "//*[(./@resource-id = 'com.android.camera2:id/shutter_button')]")
    camera_picture = (By.XPATH, "//*[(./@resource-id = 'com.android.camera2:id/progress_overlay')]")
    done_button    = (By.XPATH, "//*[(./@resource-id = 'com.android.camera2:id/done_button')]")
    cancel_button  = (By.XPATH, "//*[(./@resource-id = 'com.android.camera2:id/cancel_button')]")
    confirm_button = (By.XPATH, "//*[(./@resource-id = 'com.android.camera2:id/confirm_button')]")

    def page_wait(self):
        self.wait_element_displayed(self.shutter_button) 
        return self

    def take_photo(self):
        self.find_tapable_element(*self.camera_picture).click()
        self.find_tapable_element(*self.shutter_button).click()
        self.find_tapable_element(*self.done_button).click()

    def close_camera(self):
        self.find_tapable_element(*self.cancel_button).click()

    def tap_confirm_on_remember_photo_location(self):
        self.find_tapable_element(*self.confirm_button).click()
        return