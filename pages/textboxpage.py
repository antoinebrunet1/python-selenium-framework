from utils import driverutil


NAME_OF_FILE = "textBoxPageXpaths.properties"


def navigate_to_text_box_page(driver):
    url = "https://demoqa.com/text-box"
    driverutil.navigate_to_page(driver, url)
    driverutil.wait_for_page_to_load(driver, url)
    driverutil.take_screenshot(driver)


def enter_full_name(driver, full_name):
    driverutil.fill_field(driver, NAME_OF_FILE, "fullName", full_name)


def enter_email(driver, email):
    driverutil.fill_field(driver, NAME_OF_FILE, "email", email)


def enter_current_address(driver, current_address):
    driverutil.fill_field(driver, NAME_OF_FILE, "currentAddress", current_address)


def enter_permanent_address(driver, permanent_address):
    driverutil.fill_field(driver, NAME_OF_FILE, "permanentAddress", permanent_address)


def click_on_submit(driver):
    name_of_xpath = "submitButton"
    driverutil.scroll_down_by_number_of_pixels(driver, 150)
    driverutil.wait_for_element_to_be_clickable(driver, NAME_OF_FILE, name_of_xpath)
    driverutil.click(driver, NAME_OF_FILE, name_of_xpath)


def entered_full_name_in_box_below_submit_button(driver, full_name):
    driverutil.scroll_to_bottom_of_page(driver)
    driverutil.verify_text(driver, NAME_OF_FILE, "fullNameInBoxUnderSubmitButton", f"Name:{full_name}")


def entered_email_in_box_below_submit_button(driver, email):
    driverutil.verify_text(driver, NAME_OF_FILE, "emailInBoxUnderSubmitButton", f"Email:{email}")


def entered_current_address_in_box_below_submit_button(driver, current_address):
    driverutil.verify_text(driver, NAME_OF_FILE, "currentAddressInBoxUnderSubmitButton",
                f"Current Address :{current_address}")


def entered_permanent_address_in_box_below_submit_button(driver, permanent_address):
    driverutil.verify_text(driver, NAME_OF_FILE, "permanentAddressInBoxUnderSubmitButton",
                f"Permananet Address :{permanent_address}")
