import os
import glob
import time

ABSOLUTE_PATH_OF_DOWNLOAD_FOLDER = "C:\\Users\\Utilisateur\\PycharmProjects\\python_selenium_framework\\downloadFolder"


def clear_download_folder():
    files = glob.glob(f"{ABSOLUTE_PATH_OF_DOWNLOAD_FOLDER}\\*")

    for file in files:
        os.remove(file)


def create_download_folder_if_it_does_not_exist():
    if not os.path.exists(ABSOLUTE_PATH_OF_DOWNLOAD_FOLDER):
        os.makedirs(ABSOLUTE_PATH_OF_DOWNLOAD_FOLDER)


def file_has_been_downloaded():
    start = time.time()

    while time.time() - start < 5:
        if file_is_present_in_download_folder():
            return True

        time.sleep(0.25)

    return False


def file_is_present_in_download_folder():
    return os.path.exists(f"{ABSOLUTE_PATH_OF_DOWNLOAD_FOLDER}\\sampleFile.jpeg")
