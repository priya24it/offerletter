import pytest
import requests
import request
import time
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import with_tag_name
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.driver import ChromeDriver
import  selenium.webdriver.support.relative_locator as RelativeLocator

driver = webdriver.Chrome("C://Users//kbharathi//Desktop//MDM//WebApp//chromedriver//chromedriver.exe"
                          )

driver.get("http://live.demoguru99.com/index.php/")
driver.find_element_by_xpath("//a[contains(text(),'Mobile')]").click()
time.sleep(3)
nameLabel = driver.find_elements_by_xpath("//div[@class='sort-by']//label[1]");
driver.find_element_by_tag_name(with_tag_name("a"))
