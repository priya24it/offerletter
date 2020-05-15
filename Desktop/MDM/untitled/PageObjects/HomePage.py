import pytest
import request
import requests
import time
import pandas as pd
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from PageObjects.MobilePage import MobilePage


@pytest.mark.usefixtures("setup")
class TestLinkMobile:
    driver = None

    Mobile = (By.XPATH,"//a[contains(text(),'Mobile')]")

    def __init__(self,driver):
        self.driver=driver

    def linkmobile(self):
        self.driver.find_element(*TestLinkMobile.Mobile).click()
        mobilepage = MobilePage(self.driver)
        return mobilepage