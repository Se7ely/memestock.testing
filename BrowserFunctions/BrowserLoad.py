from selenium import webdriver
import os

class BrowserLoad:

    def FireFoxLoad(self,baseurl):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseurl)
        return driver

    def ChromeLoad(self,baseurl):
        driverlocation = "C:\\Users\\XYZ\\venv\\Lib\\site-packages\\selenium\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverlocation
        driver = webdriver.Chrome(driverlocation)
        driver.get(baseurl)
        return driver


