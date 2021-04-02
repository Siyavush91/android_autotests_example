import midhub_constants as mc

from behave import given, when, then, step
from behave import *
from utils.smart_driver import *

@then(u'I am on Main screen')
def step_impl(context):
    context.main_page.page_wait()


@when(u'I tap on Wallet tab')
def step_impl(context):
    page = context.main_page.page_wait()
    page.tap_wallet_tab()


@when(u'I tap on Docs tab')
def step_impl(context):
    page = context.main_page.page_wait()
    page.tap_docs_tab()


@when(u'I tap "Top up" button')
def step_impl(context):
    page = context.wallet_page.page_wait()
    page.tap_top_up()


@then(u'I am on Wallet screen')
def step_impl(context):
    context.wallet_page.page_wait()


@then(u'I am on Top Up Info screen')
def step_impl(context):
    context.top_up_info_page.page_wait()


@when(u'I tap "Copy" button')
def step_impl(context):
    page = context.top_up_info_page.page_wait()
    page.tap_copy()


@then(u'I verify "Wallet address" toast')
def step_impl(context):
    toast_text = context.base_page.toast_text()
    assert toast_text == mc.COPIED_WALLET_ADDRESS_TOAST
