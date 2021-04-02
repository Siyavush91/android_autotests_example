#==========================
#  Basic page
#==========================
import logging
import os
import sys
import re
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import TimeoutException
from time import sleep
from selenium.webdriver.common.by import By
from utils.logger import Logger, logger

ELEMENT_DISPLAY_TIMER      = 10
ELEMENT_DISPLAY_FAST_TIMER = 0.5
ELEMENT_DISPLAY_LONG_TIMER = 180
TIMEOUT                    = 30
ENTER_KEY_EVENT            = 66
NEXT_KEY_EVENT             = 5
CAPTURE_KEY_EVENT          = 27

class BasePage:
    progress_bar       = (By.ID, 'progressBar')

    def __init__(self, driver):
        self.driver    = driver
        self.elements  = {}
        self.elements_name = {}
        self._user     = None
        self._logger   = None
        self.action    = TouchAction(self.driver)
        self._screenshot_path = "../reports/screenshots/"
        self.device_width  = self.driver.get_window_size()['width']
        self.device_height = self.driver.get_window_size()['height']

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, ELEMENT_DISPLAY_TIMER).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            raise e

    def find_elements(self, *loc):
        try:
            WebDriverWait(self.driver, ELEMENT_DISPLAY_TIMER).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except Exception as e:
            raise e
    
    def find_element_by_xpath(self, *loc):
        try:
            WebDriverWait(self.driver, ELEMENT_DISPLAY_TIMER).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element_by_xpath(*loc)
        except Exception as e:
            raise e

    def fetch_elements_name(self, *loc, timer=ELEMENT_DISPLAY_TIMER):
        try:
            WebDriverWait(self.driver, timer).until(EC.visibility_of_element_located(loc))
            self.elements = self.driver.find_elements(*loc)
            if self.elements == None:
                return None
            for i in range(self.elements.__len__()):
                element_name_tmp = self.elements[i].get_attribute("text")
                if element_name_tmp != None:
                    self.elements_name[i] = element_name_tmp
                else:
                    sys.stdout.write("STDOUT: find search result name is null. \n")
            return self.elements_name
        except Exception as e:
            raise e

    def find_tapable_element(self, *loc):
        try:
             WebDriverWait(self.driver, ELEMENT_DISPLAY_TIMER).until(EC.element_to_be_clickable(loc))
             return self.driver.find_element(*loc)
        except Exception as e:
            raise e

    def find_the_specific_tapable_element(self, index,  *loc):
        try:
            WebDriverWait(self.driver, ELEMENT_DISPLAY_TIMER).until(EC.element_to_be_clickable(loc))
            self.elements = self.driver.find_elements(*loc)
            if self.elements == None:
                return None
            for i in range(self.elements.__len__()):
                if index == i:
                    return self.elements[index]
            self.fail("STDOUT:basepage === Can't find specific tapable element, index is %d. \n" % index)
        except Exception as e:
            raise e

    def find_first_element_name(self, *loc):
        try:
            WebDriverWait(self.driver, ELEMENT_DISPLAY_TIMER).until(EC.element_to_be_clickable(loc))
            self.elements = self.driver.find_elements(*loc)
            if self.elements == None:
                return None
            return self.elements[0].get_attribute("text")
        except Exception as e:
            raise e

    def send_keys(self, value, *loc):
        try:
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError as e:
            raise e

    def wait_element_displayed(self, loc):
        try:
            WebDriverWait(self.driver, ELEMENT_DISPLAY_TIMER).until(EC.visibility_of_element_located(loc))
        except TimeoutException:
            error_message = f" Can't find specific element, locator is {loc} "
            raise TimeoutException(error_message)

    def wait_element_not_displayed(self, loc):
        try:
            WebDriverWait(self.driver, ELEMENT_DISPLAY_LONG_TIMER).until(EC.invisibility_of_element_located(loc))
        except TimeoutException:
            error_message = f" Can't find specific element, locator is {loc} "
            raise TimeoutException(error_message)

    def wait_loader_not_displayed(self):
        self.wait_element_not_displayed(self.progress_bar)
        sleep(0.5)
        self.wait_element_not_displayed(self.progress_bar)

    def wait_elements_displayed(self, elements):
        for element in elements:
            self.wait_element_displayed(element)

    def is_element_found(self, loc):
        try:
            WebDriverWait(self.driver, ELEMENT_DISPLAY_FAST_TIMER).until(EC.visibility_of_element_located(loc))
            return True
        except TimeoutException:
            return False

    def is_tapable_element_found(self, *loc):
        try:
            EC.element_to_be_clickable(loc)
            return True
        except TimeoutException:
            return False
    
    def is_element_enabled(self, loc):
        return self.driver.find_element_by_id(loc).is_enabled()

    def send_enter_key(self):
        try:
            self.driver.keyevent(ENTER_KEY_EVENT)
        except Exception as e:
            raise e

    def run_adb_command(self, command):
        try:
            res = self.driver.execute_script("mobile: shell", {'command': command})
            return res
        except Exception as e:
            raise e

    def swipe_left(self):
        try:
            self.driver.swipe(self.device_width - 50, self.device_height / 2, 50, self.device_height / 2, 300)
        except Exception as e:
            raise e

    def swipe_right(self):
        try:
            self.driver.swipe(50, self.device_height / 2, self.device_width - 50, self.device_height / 2, 300)
        except Exception as e:
            raise e

    def swipe(self, from_x, from_y, to_x, to_y):
        try:
            self.driver.swipe(from_x, from_y, to_x, to_y, 500)
        except Exception as e:
            raise e

    def save_screenshot(self, name):
        self.driver.save_screenshot(name)   

    def toast_text(self):
        try:
             loc = (By.XPATH, "//android.widget.Toast")
             toast_text = WebDriverWait(self.driver, ELEMENT_DISPLAY_TIMER).until(EC.presence_of_element_located(loc)).get_attribute("text")
             return toast_text
        except Exception as e:
            raise e

    def scroll_down(self, locator, text=None, visibility=True):
        timeout = time.time() + TIMEOUT
        while self.element_exists(locator, text) != visibility:
            self.swipe(self.device_width / 2, self.device_height - 10, self.device_width / 2, self.device_height / 2)
            if time.time() > timeout:
                raise TimeoutException

    def scroll_up(self, locator, text=None, visibility=True):
        timeout = time.time() + TIMEOUT
        while self.element_exists(locator, text) != visibility:
            self.swipe(self.device_width / 2, self.device_height / 2, self.device_width / 2, self.device_height - 10)
            if time.time() > timeout:
                raise TimeoutException

    def element_exists(self, locator, text=None, visibility=True):
        if text == None:
            return self.is_element_found(locator)
        else:
            return text in self.fetch_elements_name(*locator).values()

    # INFO: workaround for scroll to the top of scrollview
    def scroll_to_top_of_view(self, scroll_view_locator):
        try:
            self.find_element(*scroll_view_locator).get_attribute('contentSize')
            self.swipe(self.device_width / 2, self.device_height / 2, self.device_width / 2, self.device_height - 10)
        except Exception:
            return

    def tap_device_back(self):
        self.driver.back()
        sleep(1)

    def send_app_to_background_for_5_sec(self):
        self.driver.background_app(5)

    def check_text_on_screen(self, text):
        loc = self.locator_from_text(text)
        self.find_element(*loc).click()

    def tap_next_keyboard(self):
        self.driver.execute_script('mobile: performEditorAction', {'action': 'next'})

    def tap_done_keyboard(self):
        self.driver.execute_script('mobile: performEditorAction', {'action': 'done'})

    def capture_photo(self):
        self.driver.press_keycode(CAPTURE_KEY_EVENT)

    def locator_from_text(self, text):
        xpath = f"//*[contains(@text, '{text}')]"
        return (By.XPATH, xpath)

    def open_right_menu(self):
        self.swipe(self.device_width - 1, self.device_height / 2, self.device_width / 2, self.device_height / 2)