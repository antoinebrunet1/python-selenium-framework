from utils import driverutil


NAME_OF_FILE = "buttonsPageXpaths.properties"


def navigate_to_buttons_page(driver):
    driverutil.navigate_to_page(driver, "https://demoqa.com/buttons")


def double_click_on_first_button(driver):
    driverutil.wait_for_element_to_be_clickable(driver, NAME_OF_FILE, "doubleClickButton")
    driverutil.double_click(driver, NAME_OF_FILE, "doubleClickButton")


def there_is_message_indicating_i_have_done_double_click(driver):
    driverutil.verify_text(driver, NAME_OF_FILE, "messageIndicatingIHaveDoneADoubleClick",
                "You have done a double click")


def right_click_on_second_button(driver):
    driverutil.wait_for_element_to_be_clickable(driver, NAME_OF_FILE, "rightClickButton")
    driverutil.right_click(driver, NAME_OF_FILE, "rightClickButton")


def there_is_message_indicating_i_have_done_right_click(driver):
    driverutil.verify_text(driver, NAME_OF_FILE, "messageIndicatingIHaveDoneARightClick",
                "You have done a right click")
