from selenium import webdriver
import os

class BrowserLoad:
    def FireFoxLoad(self,baseurl):
        binary='C:\\Program Files\\Mozilla Firefox\\firefox.exe'

        driver = webdriver.Firefox(firefox_binary=binary)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseurl)
        return driver
    def ChromeLoad(self,baseurl):
        driverlocation = "C:\\Users\\XYZ\\venv\\Lib\\site-packages\\selenium\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverlocation
        driver = webdriver.Chrome(driverlocation)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseurl)
        return driver

class BrowserClose:

    def __init__(self, driver):
        self.driver = driver

    def BClose(self):
        self.driver.close()