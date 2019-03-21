from selenium import webdriver
import os

def FirefoxLoad(baseurl):
    binary='C:\\Program Files\\Mozilla Firefox\\firefox.exe'
    driver = webdriver.Firefox(firefox_binary=binary)
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseurl)
    return driver

def ChromeLoad(baseurl):
    driverlocation = "C:\\Users\\XYZ\\venv\\Lib\\site-packages\\selenium\\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = driverlocation
    driver = webdriver.Chrome(driverlocation)
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseurl)
    return driver

def BrowserLoad(browser,baseurl):
    if 'chrome'in browser:
        driver=ChromeLoad(baseurl)
    else:
        driver=FirefoxLoad(baseurl)
    return driver


