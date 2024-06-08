from behave import given, when, then

from pages.toolsQa.elements.textboxpage import *


@given(u'I navigate to the text-box page')
def step_impl(context):
    navigate_to_text_box_page(context.driver)


@when(u'I enter "{full_name}" as the full name')
def step_impl(context, full_name):
    enter_full_name(context.driver, full_name)


@when(u'I enter "{email}" as the email')
def step_impl(context, email):
    enter_email(context.driver, email)


@when(u'I enter "{current_address}" as the current address')
def step_impl(context, current_address):
    enter_current_address(context.driver, current_address)


@when(u'I enter "{permanent_address}" as the permanent address')
def step_impl(context, permanent_address):
    enter_permanent_address(context.driver, permanent_address)


@when(u'I click on submit')
def step_impl(context):
    click_on_submit(context.driver)


@then(u'I see the entered full name "{full_name}" in the box below the submit button')
def step_impl(context, full_name):
    entered_full_name_in_box_below_submit_button(context.driver, full_name)


@then(u'I see the entered email "{email}" in the box below the submit button')
def step_impl(context, email):
    entered_email_in_box_below_submit_button(context.driver, email)


@then(u'I see the entered current address "{current_address}" in the box below the submit button')
def step_impl(context, current_address):
    entered_current_address_in_box_below_submit_button(context.driver, current_address)


@then(u'I see the entered permanent address "{permanent_address}" in the box below the submit button')
def step_impl(context, permanent_address):
    entered_permanent_address_in_box_below_submit_button(context.driver, permanent_address)
