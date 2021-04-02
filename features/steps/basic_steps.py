from behave import given, when, then, step
from behave import *
from utils.smart_driver import *
from selenium.webdriver.support.wait import TimeoutException

@when(u'I tap system back button')
def step_impl(context):
    context.base_page.tap_device_back()


@when(u'I fold and unfold app')
def step_impl(context):
    context.base_page.send_app_to_background_for_5_sec()


@then(u'I verify text "{text}" on the screen')
def step_impl(context, text):
    chrome_page = context.chrome_start_page
    if chrome_page.accept_button_exists():
        chrome_page.tap_accept_button()
        chrome_page.tap_no_thanks()
    context.base_page.check_text_on_screen(text)