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


@pytest.mark.usefixtures("setup")
class MobilePage:
    driver = None

    teamElement = (By.XPATH, "//body[contains(@class,'catalog-category-view categorypath-mobile-html category-mobile')]/div[@class='wrapper']/div[@class='page']/div[@class='main-container col3-layout']/div[@class='main']/div[@class='col-wrapper']/div[@class='col-main']/div[@class='category-products']/div[@class='toolbar']/div[@class='sorter']/div[@class='sort-by']/select[1]")
    listofnames = (By.XPATH, "//ul//li//div[1]//h2")

    def __init__(self, driver):
        self.driver = driver


    def hello(self):
        print("hello..")

    def getteamElement(self):
        return self.driver.find_element(*MobilePage.teamElement)

    def getlistofnames(self):
        return self.driver.find_elements(*MobilePage.listofnames)

    def listofelements(self):
        teamElement = MobilePage.getteamElement(self)
        #teamElement = MobilePage.teamElement
        time.sleep(2)
        s = Select(teamElement)
        time.sleep(3)

        s.select_by_index(1)
        elements = MobilePage.getlistofnames(self)
        l1 = []
        print(len(elements))

        for i in range(0, len(elements)):
            print(elements[i].text)
            l1.insert(i, elements[i].text)
        print(l1)

        return l1

