from utils import driverutil


NAME_OF_FILE = "tablePageXpaths.properties"


def navigate_to_table_page(driver):
    driverutil.navigate_to_page(driver, "https://demoqa.com/webtables")


def click_on_modify_for_first_row(driver):
    driverutil.wait_for_element_to_be_clickable(driver, NAME_OF_FILE, "modifyButtonForFirstRow")
    driverutil.click(driver, NAME_OF_FILE, "modifyButtonForFirstRow")


def click_on_delete_for_first_row(driver):
    driverutil.wait_for_element_to_be_clickable(driver, NAME_OF_FILE, "deleteButtonForFirstRow")
    driverutil.click(driver, NAME_OF_FILE, "deleteButtonForFirstRow")


def deleted_row_is_no_longer_present(driver):
    driverutil.wait_for_element_to_be_invisible_or_not_present(driver, NAME_OF_FILE, "firstRow")
    driverutil.take_screenshot(driver)


def change_first_name_for_first_row(driver, new_first_name):
    driverutil.wait_for_element_to_be_present(driver, NAME_OF_FILE, "windowToModifyRowsAndToAddRow")
    driverutil.clear_element(driver, NAME_OF_FILE, "firstNameInput")
    driverutil.take_screenshot(driver)
    driverutil.fill_field(driver, NAME_OF_FILE, "firstNameInput", new_first_name)
    driverutil.take_screenshot(driver)


def first_row_has_new_first_name(driver, new_first_name):
    driverutil.wait_for_element_to_be_invisible_or_not_present(driver, NAME_OF_FILE, "windowToModifyRowsAndToAddRow")
    driverutil.verify_text(driver, NAME_OF_FILE, "firstNameInTable", new_first_name)


def click_on_add(driver):
    driverutil.wait_for_element_to_be_clickable(driver, NAME_OF_FILE, "addButton")
    driverutil.click(driver, NAME_OF_FILE, "addButton")


def enter_first_name(driver, first_name):
    driverutil.wait_for_element_to_be_present(driver, NAME_OF_FILE, "windowToModifyRowsAndToAddRow")
    driverutil.fill_field(driver, NAME_OF_FILE, "firstNameInput", first_name)


def enter_last_name(driver, last_name):
    driverutil.fill_field(driver, NAME_OF_FILE, "lastNameInput", last_name)


def enter_email(driver, email):
    driverutil.fill_field(driver, NAME_OF_FILE, "emailInput", email)


def enter_age(driver, age):
    driverutil.fill_field(driver, NAME_OF_FILE, "ageInput", age)


def enter_salary(driver, salary):
    driverutil.fill_field(driver, NAME_OF_FILE, "salaryInput", salary)


def enter_department(driver, department):
    driverutil.fill_field(driver, NAME_OF_FILE, "departmentInput", department)


def first_name_of_new_row_is_correct(driver, first_name):
    driverutil.verify_text(driver, NAME_OF_FILE, "firstNameOfNewRow", first_name)


def last_name_of_new_row_is_correct(driver, last_name):
    driverutil.verify_text(driver, NAME_OF_FILE, "lastNameOfNewRow", last_name)


def age_of_new_row_is_correct(driver, age):
    driverutil.verify_text(driver, NAME_OF_FILE, "ageOfNewRow", age)


def email_of_new_row_is_correct(driver, email):
    driverutil.verify_text(driver, NAME_OF_FILE, "emailOfNewRow", email)


def salary_of_new_row_is_correct(driver, salary):
    driverutil.verify_text(driver, NAME_OF_FILE, "salaryOfNewRow", salary)


def department_of_new_row_is_correct(driver, department):
    driverutil.verify_text(driver, NAME_OF_FILE, "departmentOfNewRow", department)
