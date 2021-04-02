from behave import given, when, then, step
from behave import *
from utils.logger import Logger, logger

@given(u'I am on the {ordinal_number} Tutorial screen')
def step_impl(context, ordinal_number):
    number = to_number(ordinal_number)
    page = context.tutorial_page.page_wait()
    page.check_lexemes(number, only_title = True)


@given(u'I am on Tutorial screen')
def step_impl(context):
    context.tutorial_page.page_wait()


@then(u'I verify {ordinal_number} Tutorial screen')
def step_impl(context, ordinal_number):
    number = to_number(ordinal_number)
    context.tutorial_page.verify_page(number)

def to_number(ordinal_number):
    switcher = {
            'first' : 1,
            'second': 2,
            'third' : 3
        }
    number = switcher.get(ordinal_number, "Invalid ordinal number")
    return number


@when(u'I tap Next button')
def step_impl(context):
    page = context.tutorial_page.page_wait()
    page.tap_next_button()


@when(u'I swipe to the next Tutorial screen')
def step_impl(context):
    page = context.tutorial_page.page_wait()
    page.swipe_left()

@given(u'I tap close button')
def step_impl(context):
    page = context.tutorial_page.page_wait()
    page.tap_close_button()
    