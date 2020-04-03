import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://www.google.com")
    request.cls.driver = driver


