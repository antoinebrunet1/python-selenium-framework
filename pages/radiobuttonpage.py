from utils import driverutil


NAME_OF_FILE = "radioButtonPageXpaths.properties"


def navigate_to_radio_button_page(driver):
    driverutil.navigate_to_page(driver, "https://demoqa.com/radio-button")


def select_yes(driver):
    driverutil.wait_for_element_to_be_clickable(driver, NAME_OF_FILE, "yesButton")
    driverutil.click(driver, NAME_OF_FILE, "yesButton")


def there_is_message_indicating_i_have_selected_yes(driver):
    driverutil.verify_text(driver, NAME_OF_FILE, "messageWhenSomethingIsSelected", "You have selected Yes")
