from utils import driverutil, filesutil


NAME_OF_FILE = "uploadAndDownloadPageXpaths.properties"


def navigate_to_upload_and_download_page(driver):
    driverutil.navigate_to_page(driver, "https://demoqa.com/upload-download")


def upload_file(driver):
    absolute_path = "C:\\Users\\Utilisateur\\PycharmProjects\\python_selenium_framework\\fileForUpload.txt"
    name_of_xpath = "uploadButton"

    driverutil.upload_file(driver, NAME_OF_FILE, name_of_xpath, absolute_path)


def path_of_file_is_there(driver):
    driverutil.verify_text(driver, NAME_OF_FILE, "pathOfFile", "C:\\fakepath\\fileForUpload.txt")


def click_on_download(driver):
    filesutil.create_download_folder_if_it_does_not_exist()
    filesutil.clear_download_folder()

    name_of_xpath = "downloadButton"

    driverutil.wait_for_element_to_be_clickable(driver, NAME_OF_FILE, name_of_xpath)
    driverutil.click(driver, NAME_OF_FILE, name_of_xpath)


def file_has_been_downloaded():
    assert filesutil.file_has_been_downloaded()
