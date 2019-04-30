from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import os

baseurl='http://localhost:3000'
screenshots='D:\\Work\\University\\Spring 2019\\CMPN203\\TestingFramework\\memstock.testing\\InitialTests\\Screenshots\\'

def BrowserLoad(url=""):

    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.headless = True
    driverlocation = "C:\\Users\\XYZ\\venv\\Lib\\site-packages\\selenium\\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = driverlocation
    driver = webdriver.Chrome(driverlocation,options=options)
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseurl+url)
    return driver
    """
    binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    driver=webdriver.Firefox(firefox_binary=binary)
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseurl + url)
    return driver
    """



def Scroll(direction,driver):
    if str.lower(direction)=='up':
        driver.execute_script("window.scrollBy(0, -1000);")
    elif str.lower(direction)=='down':
        driver.execute_script("window.scrollBy(0, 1000);")

def Hover(element,driver):
    action=ActionChains(driver)
    action.move_to_element(element).perform()



