from utils import driverutil


NAME_OF_FILE = "checkBoxPageXpaths.properties"


def navigate_to_check_box_page(driver):
    driverutil.navigate_to_page(driver, "https://demoqa.com/checkbox")


def select_notes_which_is_under_desktop_which_is_under_home(driver):
    driverutil.click(driver, NAME_OF_FILE, "homeExpandButton")
    driverutil.click(driver, NAME_OF_FILE, "desktopExpandButton")
    driverutil.click(driver, NAME_OF_FILE, "notesCheckBox")


def there_is_message_indicating_i_have_selected_notes(driver):
    driverutil.verify_text(driver, NAME_OF_FILE, "firstPartOfMessageWhenSomethingIsSelected",
                "You have selected :")
    driverutil.verify_text(driver, NAME_OF_FILE, "secondPartOfMessageWhenSomethingIsSelected", "notes")
