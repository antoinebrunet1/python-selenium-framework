from selenium.webdriver.support.wait import WebDriverWait
from allure import attach
from allure_commons.types import AttachmentType
from utils.xpathspropertiesfileutil import get_xpath
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def navigate_to_page(driver, url):
    driver.get(url)


def wait_for_page_to_load(driver, url):
    WebDriverWait(driver, 5).until(
        lambda d: d.execute_script("return document.readyState") == "complete" and d.current_url == url,
        "Page not loaded"
    )


def take_screenshot(driver):
    attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


def fill_field(driver, name_of_file, name_of_xpath, text):
    xpath = get_xpath(name_of_file, name_of_xpath)

    wait_for_element_to_be_clickable(driver, name_of_file, name_of_xpath)
    driver.find_element("xpath", xpath).send_keys(text)
    take_screenshot(driver)


def wait_for_element_to_be_clickable(driver, name_of_file, name_of_xpath):
    xpath = get_xpath(name_of_file, name_of_xpath)

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, xpath)),
        f"Element with xpath {xpath} not clickable within 5 seconds"
    )


def scroll_down_by_number_of_pixels(driver, number_of_pixels):
    driver.execute_script(f'window.scrollBy(0, {number_of_pixels})')


def click(driver, name_of_file, name_of_xpath):
    driver.find_element("xpath", get_xpath(name_of_file, name_of_xpath)).click()


def scroll_to_bottom_of_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def verify_text(driver, name_of_file, name_of_xpath, expected_text):
    assert driver.find_element("xpath", get_xpath(name_of_file, name_of_xpath)).text == expected_text
    take_screenshot(driver)
