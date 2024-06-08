# Task 25, In the IMDb webpage fill the data on the webpage

import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *


# Explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# exceptions
from selenium.common.exceptions import *


class Submit:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))

        # implementation of explicit wait
        self.wait = WebDriverWait(self.driver, 10)

    def boot(self):
        """
        This method will open the chrome web-browser with the url passed
        :return:
        """
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.wait.until(EC.url_to_be(self.url))

    def quit(self):
        self.driver.quit()

    def findElementByNAME(self, NAME):
        return self.driver.find_element(by=By.NAME, value=NAME)

    def login(self):
        self.boot()
        # After the booting below locater is used to Click on the Expand all Button
        try:
            self.driver.find_element(
                By.XPATH, value='//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/div/button').click()

            # Here we are locating the element by name and pass the value " Vijay" using send key
            try:
                self.wait.until(EC.presence_of_element_located(
                    (By.NAME, "name-text-input"))).send_keys("Vijay")

            except ElementNotInteractableException as e:
                print("'name-text-input' - element not interactable")

            # Here we are locating the element by name and pass the date of birth using send key
            try:
                self.wait.until(EC.presence_of_element_located(
                    (By.NAME, "birth-year-month-start-input"))).send_keys("1974-06")
                self.wait.until(EC.presence_of_element_located(
                    (By.NAME, "birth-year-month-end-input"))).send_keys("1974-06")
            except ElementNotInteractableException as e:
                print("'birth-year-month-start-input' - element not interactable")


            # After filled the required the information and again clicked on the expand all button
            # because after clicking the button only the Search Button is enabled for us
            self.driver.find_element(
                By.XPATH,
                value='//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/div/button').click()

            # This is used to click the Search button on the webpage

            self.driver.find_element(
                By.XPATH, value='//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button').click()
        except NoSuchElementException as e:
            print(e)
        finally:
            self.quit()


if __name__ == "__main__":
    obj = Submit('https://www.imdb.com/search/name/')
    obj.login()
