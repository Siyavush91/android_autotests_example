from behave import given, when, then, step
from behave import *
from utils.smart_driver import *
from selenium.webdriver.support.wait import TimeoutException
from time import sleep


@when("I tap search button")
def step_impl(context):
    page = context.choose_domain_page.page_wait()
    page.tap_search_btn()


@step('I enter "{value}" in search field')
def step_impl(context, value):
    page = context.choose_domain_page.page_wait()
    context.choose_domain_page.verify_keyboard()
    page.enter_search(value)


@then('I verify "{value}" on screen')
def step_impl(context, value):
    context.choose_domain_page.verify_domain(value)


@when("I tap clear button")
def step_impl(context):
    context.choose_domain_page.tap_clear_search_btn()


@then('I verify screen has message "Ничего не найдено"')
def step_impl(context):
    context.choose_domain_page.verify_not_found_msg()


@then("I verify text in search field")
def step_impl(context):
    context.choose_domain_page.verify_header()


@then("I verify header on screen")
def step_impl(context):
    context.choose_domain_page.verify_header()


@step("Scroll to a particular domain")
def step_impl(context):
    page = context.choose_domain_page.page_wait()
    page.scroll_down_to_domain()
