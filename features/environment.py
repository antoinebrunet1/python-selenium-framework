from behave.model_core import Status
from selenium import webdriver

import utils.filesutil
import utils.driverutil


def before_scenario(context, scenario):
    prefs = {"download.default_directory": utils.filesutil.ABSOLUTE_PATH_OF_DOWNLOAD_FOLDER}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", prefs)
    context.driver = webdriver.Chrome(options=options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)


def after_scenario(context, scenario):
    if scenario.status == Status.failed:
        utils.driverutil.take_screenshot(context.driver)

    context.driver.close()
