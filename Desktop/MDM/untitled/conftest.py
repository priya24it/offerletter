import pytest
import requests
import request
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.driver import ChromeDriver


@pytest.fixture(scope="class")
def setup(request):
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-notifications')

    capa = DesiredCapabilities.CHROME
    #capa["pageLoadStrategy"] = "none"

    #prefs = {'profile.default_content_setting_values.notifications': 2}
    #options.add_experimental_option('prefs', prefs)

    driver = webdriver.Chrome("C://Users//kbharathi//Desktop//MDM//WebApp//chromedriver//chromedriver.exe",chrome_options=options,desired_capabilities=capa)

   # driver.get("https://www.mysmartprice.com/mobile/apple-iphone-7-msp10208")
    driver.get("https://www.softwaretestingmaterial.com/")
    #driver.get("https://www.guru99.com/")
    request.cls.driver = driver
    #driver.find_element_by_partial_link_text()
    driver.maximize_window()



    #capabilities = DesiredCapabilities.CHROME.copy()
   # webdriver.DesiredCapabilities.CHROME.copy()
   # webdriver.ChromeOptions()




    yield
    driver.close()

@pytest.fixture(params = [(1,2),(3,4)])
def addidtion(request):
    return request.param





