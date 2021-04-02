from behave import given, when, then, step
from behave import *
from utils.smart_driver import *
from selenium.webdriver.support.wait import TimeoutException
from time import sleep

import time

@when(u'I tap on Checking Docs Tab')
def step_impl(context):
    page = context.my_docs_page.page_wait()
    page.tap_checking_docs_tab()


@when(u'I tap on Ready Docs Tab')
def step_impl(context):
    page = context.my_docs_page.page_wait()
    page.tap_ready_docs_tab()


@then(u'I verify My Docs screen')
def step_impl(context):
    context.my_docs_page.verify_page()


@then(u'I am on My Docs screen')
def step_impl(context):
    context.my_docs_page.page_wait()


@then(u'I verify {state}Ready Docs Section')
def step_impl(context, state):
    page = context.my_docs_page
    page.verify_page()
    if state == 'empty ':
        page.verify_empty_state('Ready')


@then(u'I verify {state}Checking Docs Section')
def step_impl(context, state):
    page = context.my_docs_page
    page.verify_page()
    if state == 'empty ':
        page.verify_empty_state('Checking')


@then(u'I verify "{doc_name}" doc is in status "{status}"')
def step_impl(context, doc_name, status):
    page = context.my_docs_page
    page.verify_doc_status(doc_name, status)


@when(u'I open "{doc_name}"')
def step_impl(context, doc_name):
    page = context.my_docs_page.page_wait()
    page.open_doc(doc_name)  


@when(u'I tap on "Add doc" button')
def step_impl(context):
    page = context.my_docs_page.page_wait()
    page.tap_add_doc_button()


@then(u'I verify Choose Domen screen')
def step_impl(context):
    context.choose_domain_page.verify_page()


@when(u'I choose "{name}" option on Choose Domen screen')
def step_impl(context, name):
    page = context.choose_domain_page.page_wait()
    page.tap_domain(name)


@then(u'I am on Add Doc screen')
def step_impl(context):
    context.add_doc_page.page_wait()


@then(u'I verify following elements in list on Add Doc screen')
def step_impl(context):
    for row in context.table:
        context.add_doc_page.verify_list_element(row['name'], row['value'])


@when(u'I choose "{name}" option on Add Doc screen')
def step_impl(context, name):
    page = context.add_doc_page.page_wait()
    page.tap_option(name)


@then(u'I verify Verification Type screen')
def step_impl(context):
    page = context.verification_type_page
    for row in context.table:
        if row['attribute'] == 'header':
            name = row['value']
    page.verify_page(name)


@then(u'I am on Verification Type screen')
def step_impl(context):
    context.verification_type_page.page_wait()


@when(u'I choose global green verification on Verification Type screen')
def step_impl(context):
    page = context.verification_type_page.page_wait()
    page.tap_choose_global_green_verification()


@when(u'I choose global yellow verification on Verification Type screen')
def step_impl(context):
    page = context.verification_type_page.page_wait()
    page.tap_choose_global_yellow_verification()


@when(u'I tap Details button for yellow verification')
def step_impl(context):
    page = context.verification_type_page.page_wait()
    page.tap_details_global_yellow_verification()


@then(u'I verify not supported verification alert')
def step_impl(context):
    context.verification_type_page.verify_not_supported_verification_alert()


@when(u'I tap on OK button on not supported verification alert')
def step_impl(context):
    context.verification_type_page.close_not_supported_verification_alert()


@then(u'I verify Verification Details screen')
def step_impl(context):
    context.verification_details_page.verify_page()


@when(u'I choose verification on Verification Details screen')
def step_impl(context):
    page = context.verification_details_page.page_wait()
    page.tap_choose_button()


@when(u'I tap back button on Verification Details screen')
def step_impl(context):
    page = context.verification_details_page.page_wait()
    page.tap_back_button()


@then(u'I verify Add Doc Form page with following attributes')
def step_impl(context):
    page = context.add_doc_form_page
    add_photo_button_state = None
    for row in context.table:
        if row['attribute'] == 'type':
            page_type = row['value']
        elif row['attribute'] == 'photo_hint':
            page.verify_photo_hint(row['value'])
        elif row['attribute'] == 'photo_header':
            page.verify_photo_page_header_lexeme(row['value'])
        elif row['attribute'] == 'add_photo':
            add_photo_button_state = row['value']
    page.verify_page(page_type, add_photo_button_state)


@then(u'I verify {current} page out of {overall} page Add Doc Form Screen with name "{name}"')
def step_impl(context, current, overall, name):
    page = context.add_doc_form_page
    page.verify_page(current, overall, name)
    if page.next_button_exists() == True:
        page.verify_next_button()
    else:
        page.scroll_down_to_next()
        page.verify_next_button()
        page.scroll_to_the_top()


@then(u'I verify following fields on Add Doc Form Screen')
def step_impl(context):
    page = context.add_doc_form_page.page_wait()
    for row in context.table:
        if page.field_displayed(row['name']):
            page.verify_field(row['name'])
        else:
            page.scroll_down_to_field(row['name'])
            page.verify_field(row['name'])
    page.scroll_to_the_top()


@when(u'I scroll down to agreement')
def step_impl(context):
    page = context.add_doc_form_page.page_wait()
    page.scroll_to_the_bottom()


@when(u'I tap on agreement link')
def step_impl(context):
    page = context.add_doc_form_page.page_wait()
    page.tap_on_agreement_link()


@when(u'I tap on "{field}" field on Add Doc Form Screen')
def step_impl(context, field):
    page = context.add_doc_form_page.page_wait()
    page.tap_field(field)


@when(u'I tap on the first field on Add Doc Form Screen')
def step_impl(context):
    page = context.add_doc_form_page.page_wait()
    page.tap_first_field()


@then(u'I verify field "{field}" has warning "{warning}"')
def step_impl(context, field, warning):
    page = context.add_doc_form_page.page_wait()
    page.verify_warning_for_field(field, warning)


@then(u'I verify {number} fields have warning "{warning}"')
def step_impl(context, number, warning):
    page = context.add_doc_form_page.page_wait()
    page.verify_warning_for_fields(number, warning)


@then(u'I verify field "{field}" has no warning')
def step_impl(context, field):
    page = context.add_doc_form_page.page_wait()
    page.verify_no_warning_for_field(field)


@then(u'I verify all fields have no warning')
def step_impl(context):
    page = context.add_doc_form_page.page_wait()    
    page.verify_no_warning_for_all_fields()


@then(u'I verify mask hint "{mask}"')
def step_impl(context, mask):
    page = context.field_page.page_wait()
    page.verify_mask_hint(mask)


@when(u'I fill out following fields on Field Screen')
def step_impl(context):
    # Table with name, value, type, after_mask header
    overall = len(list(context.table))
    for idx, row in enumerate(context.table):
        page = context.field_page.page_wait()
        page.verify_content(row['type'], row['name'])
        page.verify_step_screen(idx + 1, overall)
        if row['after_mask'] != '':
            page.fill_field(row['type'], row['value'], row['after_mask'])
        else:
            page.fill_field(row['type'], row['value'])


@when(u'I fill out following field on Field Screen without confirmation')
def step_impl(context):
    # Table with name, value, type
    page = context.field_page.page_wait()
    for row in context.table:
        if row['type'] == 'Text' or row['type'] == 'Number':
            page.fill_text_field(row['value'])
        elif row['type'] == 'Checkbox':
            page.fill_checkbox_field(row['value'])
        elif row['type'] == 'Date':
            page.fill_date_field(row['value'])
        else:
            raise('Unsupported type of field')

@then(u'I verify "{field}" {type_field} field is {current_step} step out of {overall}')
def step_impl(context, field, type_field, current_step, overall):
    page = context.field_page.page_wait()
    page.verify_step_screen(current_step, overall)
    if type_field == 'text':
        page.verify_text_form(field, False)
    elif type_field == 'option':
        page.verify_checkbox_form(field)
    elif type_field == 'date':
        page.verify_date_form(field, False)
    else:
        raise('Unsupported type of field')


@when(u'I tap on confirm button on Field Screen')
def step_impl(context):
    page = context.field_page.page_wait()
    page.tap_confirm_button()


@when(u'I tap on previous step button on Field Screen')
def step_impl(context):
    page = context.field_page.page_wait()
    page.tap_previous_step_button()


@when(u'I tap back button on Field Screen')
def step_impl(context):
    page = context.field_page.page_wait()
    page.tap_back_button()


@when(u'I clean field on Field Screen')
def step_impl(context):
    page = context.field_page.page_wait()
    page.clean_field()


@when(u'I tap next button on Add Doc Form Screen')
def step_impl(context):
    page = context.add_doc_form_page.page_wait()
    page.tap_next_button()


@then(u'I verify {number} attached photo')
def step_impl(context, number):
    page = context.add_doc_form_page.page_wait()
    page.check_attached_photo(number)


@when(u'I tap Add Photo button')
def step_impl(context):
    page = context.add_doc_form_page.page_wait()
    page.tap_add_photo_button()


@when(u'I tap back button on Add Doc Form Screen')
def step_impl(context):
    page = context.add_doc_form_page.page_wait()
    page.tap_back()

    
@when(u'I give all requested permissions')
def step_impl(context):
    permission_alert_page = context.permission_alert
    permission_alert_page.page_wait()
    permission_alert_page.tap_allow()
    if permission_alert_page.permission_exists():
        permission_alert_page.tap_allow()
        context.camera_page.tap_confirm_on_remember_photo_location()
        sleep(1)
        context.base_page.tap_device_back()
        context.add_doc_form_page.page_wait().tap_add_photo_button()


@when(u'I take a photo')
def step_impl(context):
    page = context.camera_page.page_wait()
    page.take_photo()


@then(u'I am on Camera screen')
def step_impl(context):
    context.camera_page.page_wait()

@when(u'I attach {number} photos on Attach Doc screen')
def step_impl(context, number):
    for x in range(0, int(number)):
        add_doc_form_page = context.add_doc_form_page.page_wait()
        add_doc_form_page.tap_add_photo_button()
        camera_page = context.camera_page.page_wait()
        camera_page.take_photo()
        context.add_doc_form_page.page_wait()


@when(u'I tap on agreement switch')
def step_impl(context):
    page = context.add_doc_form_page.page_wait()
    page.tap_agreement_switch()


@when(u'I tap Next button on Attach Doc screen')
def step_impl(context):
    page = context.add_doc_form_page.page_wait()
    page.tap_next_button()


@then(u'I verify "{message}" warning on Attach Doc screen')
def step_impl(context, message):
    page = context.add_doc_form_page.page_wait()
    page.verify_photo_warning(message)

    
@then(u'I wait when loader disappeared on Add Doc Form screen')
def step_impl(context):
    context.add_doc_form_page.wait_loader_not_displayed()


@then(u'I verify Request In Progress screen')
def step_impl(context):
    page = context.request_in_progress_page.page_wait()
    page.verify_page()


@when(u'I close Request In Progress screen')
def step_impl(context):
    page = context.request_in_progress_page.page_wait()
    page.tap_back()
