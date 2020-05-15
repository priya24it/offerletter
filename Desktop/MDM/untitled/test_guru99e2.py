
import pytest
import request
import requests
import time
import pandas as pd
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from PageObjects.HomePage import TestLinkMobile
#from selenium.webdriver.support.relative_locator  import  with_tag_name



@pytest.mark.usefixtures("setup")
class TestGuru99:

    @pytest.mark.skip
    def test_sort(self):
        print("statred")
        HomePageLinkMobile = TestLinkMobile(self.driver)
        mobilepage = HomePageLinkMobile.linkmobile()
        print("mobile page has executed successfully...")
        print(mobilepage.listofelements())
       # teamElement = mobilepage.getteamElement()
        #time.sleep(2)
        #print(teamElement)
        #s = Select(teamElement)
        #time.sleep(3)

        #s.select_by_index(1)
        #time.sleep(3)
        #elements = mobilepage.getlistofnames()
        #l1 = []
        #for i in range(0, len(elements)):
            #print(elements[i].text)
            #l1.insert(i, elements[i].text)
        #print(l1)
        #l2 = ['1', '2', '3']
        #assert l1 == l2, 'pass'
        l1 = mobilepage.listofelements()
        print(l1)
        l2 = ['1', '2', '3']
        assert l1 == l2, 'pass'


    @pytest.mark.skip
    def test_sonyXperiaPrice(self):
        print("statred")
        HomePageLinkMobile = TestLinkMobile(self.driver)
        mobilepage = HomePageLinkMobile.linkmobile()
        print("mobile page has executed successfully...")
        teamElement = self.driver.find_element_by_xpath("//body[contains(@class,'catalog-category-view categorypath-mobile-html category-mobile')]/div[@class='wrapper']/div[@class='page']/div[@class='main-container col3-layout']/div[@class='main']/div[@class='col-wrapper']/div[@class='col-main']/div[@class='category-products']/div[@class='toolbar']/div[@class='sorter']/div[@class='sort-by']/select[1]")
        # teamElement = MobilePage.teamElement
        time.sleep(2)
        s = Select(teamElement)
        time.sleep(3)

        s.select_by_index(1)
        elements = self.driver.find_elements_by_xpath("//ul//li//div[1]//h2")
        l1 = []
        print(len(elements))
        for i in range(0, len(elements)):
            requiredelement = elements[i]
           # print(elements[i].text)
            if elements[i].text in "SONY XPERIA":
                print("sony...")
                print(elements[i])
                print(elements[i].text)
                price = elements[i].find_element_by_xpath("//parent::h2[@class='product-name']//parent::div[@class='product-info']/div[@class='price-box']//span[contains(text(),'$100.00')]").text
                print(price)
                parentelement = elements[i].find_element_by_xpath("//parent::h2[@class='product-name']//a[contains(text(),'Sony Xperia')]")
                parentelement.click()



                print(parentelement)
                break

        print("")
        wait = WebDriverWait(self.driver,5)
        wait.until(EC.presence_of_element_located((By.XPATH,"//span[@class='price']")))

        price = self.driver.find_element_by_xpath("//span[@class='price']").text
        print(price)


    @pytest.mark.skip
    def test_sonyXperiaaddtoCart(self):
        print("statred")
        HomePageLinkMobile = TestLinkMobile(self.driver)
        mobilepage = HomePageLinkMobile.linkmobile()
        print("mobile page has executed successfully...")
        teamElement = self.driver.find_element_by_xpath(
            "//body[contains(@class,'catalog-category-view categorypath-mobile-html category-mobile')]/div[@class='wrapper']/div[@class='page']/div[@class='main-container col3-layout']/div[@class='main']/div[@class='col-wrapper']/div[@class='col-main']/div[@class='category-products']/div[@class='toolbar']/div[@class='sorter']/div[@class='sort-by']/select[1]")
        # teamElement = MobilePage.teamElement
        time.sleep(2)
        s = Select(teamElement)
        time.sleep(3)

        s.select_by_index(1)
        elements = self.driver.find_elements_by_xpath("//ul//li//div[1]//h2")
        l1 = []
        print(len(elements))
        for i in range(0, len(elements)):
            requiredelement = elements[i]
            # print(elements[i].text)
            if elements[i].text in "SONY XPERIA":
                print("sony...")
                print(elements[i])
                print(elements[i].text)
                #elements[i].find_elements_by_xpath("//parent::h2[@class='product-name']")
                elements[i].find_element_by_xpath("//parent::h2[@class='product-name']//parent::div[@class='product-info']//div[@class='actions']//button").click()

                self.driver.find_element_by_xpath("//input[@title='Qty']").send_keys(1000)
                self.driver.find_element_by_xpath("//input[@title='Qty']").click()
                time.sleep(3)
                error_message = self.driver.find_element_by_xpath("//span[contains(text(),'Some of the products cannot be ordered in requeste')]").text
                print(error_message)

    def test_selenium4(self):
        print("started")
        print("statred")
        HomePageLinkMobile = TestLinkMobile(self.driver)
        mobilepage = HomePageLinkMobile.linkmobile()
        print("mobile page has executed successfully...")
        nameLabel = self.driver.find_elements_by_xpath("//div[@class='sort-by']//label[1]");
        self.driver.find_element(with_tag_name("select").toRightOf(nameLabel));























