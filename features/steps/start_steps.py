import midhub_constants as mc
import random

from behave import given, when, then, step
from behave import *
from utils.smart_driver import *
from time import sleep

@then(u'I am on Start screen')
def step_impl(context):
    context.start_page.page_wait()


@then(u'I verify Start screen')
def step_impl(context):
    context.start_page.verify_page()


@when(u'I tap "Create account" button')
def step_impl(context):
    page = context.start_page.page_wait()
    page.tap_create_acc()


@then(u'I am on Pin Code screen')
def step_impl(context):
    context.pin_code_page.page_wait()


@then(u'I verify Pin Code screen')
def step_impl(context):
    context.pin_code_page.verify_page()


@when(u'I enter "{code}" on Pin Code screen')
def step_impl(context, code):
    page = context.pin_code_page.page_wait()
    page.enter_pin_code(code)


@when(u'I enter random code on Pin Code screen')
def step_impl(context):
    page = context.pin_code_page.page_wait()
    code = random.randint(1000,9999)
    page.enter_pin_code(code)


@when(u'I tap "Log in" button on Pin Code screen')
def step_impl(context):
    page = context.pin_code_page.page_wait()
    assert page.login_button_tappable()
    page.tap_login()


@then(u'I verify Wallet Info screen')
def step_impl(context):
    context.wallet_info_page.verify_page()


@then(u'I am on Wallet Info screen')
def step_impl(context):
    context.wallet_info_page.page_wait()


@when(u'I tap "Next" button')
def step_impl(context):
    page = context.wallet_info_page.page_wait()
    page.tap_next()


@then(u'I wait when loader disappeared')
def step_impl(context):
    context.base_page.wait_loader_not_displayed()
