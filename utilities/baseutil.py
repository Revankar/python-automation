import inspect
import logging
import time
import pytest
from selenium.common import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class Base:

    def click(self,locator,retries=2, delay=2):
        attempt = 0
        while attempt < retries:
            try:
                element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
                element.click()
                return  # Exit function if successful
            except (TimeoutException, NoSuchElementException) as e:
                if attempt == retries - 1:
                    raise NoSuchElementException(f"Element {locator} not found after {retries} attempts - FAIL")
            except StaleElementReferenceException:
                if attempt == retries - 1:
                    raise StaleElementReferenceException(
                        f"Element {locator} became stale after {retries} attempts - FAIL")

            attempt += 1
            time.sleep(delay)  # Wait before retrying

    def click1(self,locator):
        try:
            ele = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].click();",ele)
        except (TimeoutException, NoSuchElementException) as e:
            raise NoSuchElementException(f"Element {locator} not found - FAIL")

    def getText(self,locator,retries=2, delay=2):
        attempt = 0
        while attempt < retries:
            try:
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
                text = element.text.strip() # Strip spaces for cleaner output
                return text if text else None  # Return None if empty text
            except (TimeoutException, NoSuchElementException) as e:
                if attempt == retries - 1:
                    raise NoSuchElementException(f"Element {locator} not found after {retries} attempts - FAIL")
            except StaleElementReferenceException:
                if attempt == retries - 1:
                    raise StaleElementReferenceException(
                        f"Element {locator} became stale after {retries} attempts - FAIL")

            attempt += 1
            time.sleep(delay)  # Wait before retrying

        return None

    def sendText(self,locator,text,retries=2,delay=2):
        attempt = 0
        while attempt < retries:
            try:
                ele = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
                ele.send_keys(text)
                return True  # Exit function if successful
            except (TimeoutException, NoSuchElementException) as e:
                if attempt == retries - 1:
                    raise NoSuchElementException(f"Element {locator} not found after {retries} attempts - FAIL")
            except StaleElementReferenceException:
                if attempt == retries - 1:
                    raise StaleElementReferenceException(
                        f"Element {locator} became stale after {retries} attempts - FAIL")
            except ElementNotInteractableException:
                if attempt == retries - 1:
                    raise ElementNotInteractableException(
                        f"Element {locator} is not interactable after {retries} attempts - FAIL")

            attempt += 1
            time.sleep(delay)  # Wait before retrying
        return False  # Return False if all attempts fail

    def clearAndSendText(self,locator,text):
        try:
            ele = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(locator))
            ele.click()
            ele.clear()
            time.sleep(10)
            ele.send_keys(text)
        except (TimeoutException, NoSuchElementException) as e:
            raise NoSuchElementException(f"Element {locator} not found - FAIL")

# Logger
    @staticmethod
    def getLogger():
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        if not logger.handlers:
            filehandler = logging.FileHandler('logfile.log')
            formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(funcName)s - %(message)s")
            filehandler.setFormatter(formatter)
            logger.addHandler(filehandler)
            logger.setLevel(logging.INFO)
        return logger
