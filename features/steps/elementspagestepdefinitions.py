from behave import given, when, then

from pages import uploadanddownloadpage, checkboxpage, buttonspage, tablepage, radiobuttonpage, textboxpage


@given(u'I navigate to the text-box page')
def step_impl(context):
    textboxpage.navigate_to_text_box_page(context.driver)


@when(u'I enter "{full_name}" as the full name')
def step_impl(context, full_name):
    textboxpage.enter_full_name(context.driver, full_name)


@when(u'I enter "{email}" as the email')
def step_impl(context, email):
    tablepage.enter_email(context.driver, email)


@when(u'I enter "{current_address}" as the current address')
def step_impl(context, current_address):
    textboxpage.enter_current_address(context.driver, current_address)


@when(u'I enter "{permanent_address}" as the permanent address')
def step_impl(context, permanent_address):
    textboxpage.enter_permanent_address(context.driver, permanent_address)


@when(u'I click on submit')
def step_impl(context):
    textboxpage.click_on_submit(context.driver)


@then(u'I see the entered full name "{full_name}" in the box below the submit button')
def step_impl(context, full_name):
    textboxpage.entered_full_name_in_box_below_submit_button(context.driver, full_name)


@then(u'I see the entered email "{email}" in the box below the submit button')
def step_impl(context, email):
    textboxpage.entered_email_in_box_below_submit_button(context.driver, email)


@then(u'I see the entered current address "{current_address}" in the box below the submit button')
def step_impl(context, current_address):
    textboxpage.entered_current_address_in_box_below_submit_button(context.driver, current_address)


@then(u'I see the entered permanent address "{permanent_address}" in the box below the submit button')
def step_impl(context, permanent_address):
    textboxpage.entered_permanent_address_in_box_below_submit_button(context.driver, permanent_address)


@given(u'I navigate to the check box page')
def step_impl(context):
    checkboxpage.navigate_to_check_box_page(context.driver)


@when(u'I select Notes which is under Desktop which is under Home')
def step_impl(context):
    checkboxpage.select_notes_which_is_under_desktop_which_is_under_home(context.driver)


@then(u'I see the message indicating I have selected Notes')
def step_impl(context):
    checkboxpage.there_is_message_indicating_i_have_selected_notes(context.driver)


@given(u'I navigate to the radio button page')
def step_impl(context):
    radiobuttonpage.navigate_to_radio_button_page(context.driver)


@when(u'I select Yes')
def step_impl(context):
    radiobuttonpage.select_yes(context.driver)


@then(u'I see the message indicating I have selected Yes')
def step_impl(context):
    radiobuttonpage.there_is_message_indicating_i_have_selected_yes(context.driver)


@given(u'I navigate to the table page')
def step_impl(context):
    tablepage.navigate_to_table_page(context.driver)


@when(u'I click on modify for the first row')
def step_impl(context):
    tablepage.click_on_modify_for_first_row(context.driver)


@when(u'I click on delete for the first row')
def step_impl(context):
    tablepage.click_on_delete_for_first_row(context.driver)


@then(u'I see the row I deleted is no longer present')
def step_impl(context):
    tablepage.deleted_row_is_no_longer_present(context.driver)


@when(u'I change the first name to "{new_first_name}"')
def step_impl(context, new_first_name):
    tablepage.change_first_name_for_first_row(context.driver, new_first_name)


@then(u'I see the first row now has the first name "{new_first_name}"')
def step_impl(context, new_first_name):
    tablepage.first_row_has_new_first_name(context.driver, new_first_name)


@when(u'I click on add')
def step_impl(context):
    tablepage.click_on_add(context.driver)


@when(u'I enter "{first_name}" for the first name')
def step_impl(context, first_name):
    tablepage.enter_first_name(context.driver, first_name)


@when(u'I enter "{last_name}" for the last name')
def step_impl(context, last_name):
    tablepage.enter_last_name(context.driver, last_name)


@when(u'I enter "{email}" for the email')
def step_impl(context, email):
    tablepage.enter_email(context.driver, email)


@when(u'I enter "{age}" for the age')
def step_impl(context, age):
    tablepage.enter_age(context.driver, age)


@when(u'I enter "{salary}" for the salary')
def step_impl(context, salary):
    tablepage.enter_salary(context.driver, salary)


@when(u'I enter "{department}" for the department')
def step_impl(context, department):
    tablepage.enter_department(context.driver, department)


@then(u'I see the first name of the new row is "{first_name}"')
def step_impl(context, first_name):
    tablepage.first_name_of_new_row_is_correct(context.driver, first_name)


@then(u'I see the last name of the new row is "{last_name}"')
def step_impl(context, last_name):
    tablepage.last_name_of_new_row_is_correct(context.driver, last_name)


@then(u'I see the age of the new row is "{age}"')
def step_impl(context, age):
    tablepage.age_of_new_row_is_correct(context.driver, age)


@then(u'I see the email of the new row is "{email}"')
def step_impl(context, email):
    tablepage.email_of_new_row_is_correct(context.driver, email)


@then(u'I see the salary of the new row is "{salary}"')
def step_impl(context, salary):
    tablepage.salary_of_new_row_is_correct(context.driver, salary)


@then(u'I see the department of the new row is "{department}"')
def step_impl(context, department):
    tablepage.department_of_new_row_is_correct(context.driver, department)


@given(u'I navigate to the buttons page')
def step_impl(context):
    buttonspage.navigate_to_buttons_page(context.driver)


@when(u'I double click on the first button')
def step_impl(context):
    buttonspage.double_click_on_first_button(context.driver)


@then(u'I see the message indicating I have done a double click')
def step_impl(context):
    buttonspage.there_is_message_indicating_i_have_done_double_click(context.driver)


@when(u'I right click on the second button')
def step_impl(context):
    buttonspage.right_click_on_second_button(context.driver)


@then(u'I see the message indicating I have done a right click')
def step_impl(context):
    buttonspage.there_is_message_indicating_i_have_done_right_click(context.driver)


@given(u'I navigate to the upload and download page')
def step_impl(context):
    uploadanddownloadpage.navigate_to_upload_and_download_page(context.driver)


@when(u'I upload a file')
def step_impl(context):
    uploadanddownloadpage.upload_file(context.driver)


@then(u'I see the path of the file')
def step_impl(context):
    uploadanddownloadpage.path_of_file_is_there(context.driver)


@when(u'I click on download')
def step_impl(context):
    uploadanddownloadpage.click_on_download(context.driver)


@then(u'I see that the file is downloaded')
def step_impl(context):
    uploadanddownloadpage.file_has_been_downloaded()
