from utils.driverutil import (navigate_to_page, wait_for_page_to_load, take_screenshot, fill_field,
                              scroll_down_by_number_of_pixels, wait_for_element_to_be_clickable, click, verify_text,
                              scroll_to_bottom_of_page)


name_of_file = "textBoxPageXpaths.properties"


def navigate_to_text_box_page(driver):
    url = "https://demoqa.com/text-box"
    navigate_to_page(driver, url)
    wait_for_page_to_load(driver, url)
    take_screenshot(driver)


def enter_full_name(driver, full_name):
    fill_field(driver, name_of_file, "fullName", full_name)


def enter_email(driver, email):
    fill_field(driver, name_of_file, "email", email)


def enter_current_address(driver, current_address):
    fill_field(driver, name_of_file, "currentAddress", current_address)


def enter_permanent_address(driver, permanent_address):
    fill_field(driver, name_of_file, "permanentAddress", permanent_address)


def click_on_submit(driver):
    name_of_xpath = "submitButton"
    scroll_down_by_number_of_pixels(driver, 150)
    wait_for_element_to_be_clickable(driver, name_of_file, name_of_xpath)
    click(driver, name_of_file, name_of_xpath)


def entered_full_name_in_box_below_submit_button(driver, full_name):
    scroll_to_bottom_of_page(driver)
    verify_text(driver, name_of_file, "fullNameInBoxUnderSubmitButton", f"Name:{full_name}")


def entered_email_in_box_below_submit_button(driver, email):
    verify_text(driver, name_of_file, "emailInBoxUnderSubmitButton", f"Email:{email}")


def entered_current_address_in_box_below_submit_button(driver, current_address):
    verify_text(driver, name_of_file, "currentAddressInBoxUnderSubmitButton",
                f"Current Address :{current_address}")


def entered_permanent_address_in_box_below_submit_button(driver, permanent_address):
    verify_text(driver, name_of_file, "permanentAddressInBoxUnderSubmitButton",
                f"Permananet Address :{permanent_address}")
