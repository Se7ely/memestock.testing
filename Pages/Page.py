from GeneralUtilities import BrowserFunctions
from selenium import webdriver
class Page():



    def __init__(self):
        self.url=''


    def Redirect(self,driver):

        driver.get(BrowserFunctions.baseurl+self.url)

    def IsOn(self,driver):
        return driver.current_url==BrowserFunctions.baseurl+self.url
