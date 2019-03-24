from selenium import webdriver
import os
from selenium.webdriver import ActionChains

baseurl='http://localhost:3000'


def FirefoxLoad(url):
    binary='C:\\Program Files\\Mozilla Firefox\\firefox.exe'
    driver = webdriver.Firefox(firefox_binary=binary)
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseurl+url)
    return driver

def ChromeLoad(url):
    driverlocation = "C:\\Users\\XYZ\\venv\\Lib\\site-packages\\selenium\\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = driverlocation
    driver = webdriver.Chrome(driverlocation)
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseurl+url)
    return driver

def BrowserLoad(browser='chrome',url=''):
    if 'chrome'in browser:
        driver=ChromeLoad(url)
    else:
        driver=FirefoxLoad(url)
    return driver

def Scroll(direction,driver):
    if str.lower(direction)=='up':
        driver.execute_script("window.scrollBy(0, -1000);")
    elif str.lower(direction)=='down':
        driver.execute_script("window.scrollBy(0, 1000);")

def Hover(element,driver):
    action=ActionChains(driver)
    action.move_to_element(element).perform()



