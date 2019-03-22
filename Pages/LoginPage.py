from selenium import webdriver
from GeneralUtilities import BrowserFunctions


class LoginPage():
    url='http://localhost:3000/Login/'

    def __init__(self,driver):
        self.driver=driver
        self.usernamefield=self.driver.find_element_by_xpath('//input[@placeholder="User name"]')
        self.passwordfield=self.driver.find_element_by_xpath('//input[@placeholder="Password"]')
        self.loginbutton=self.driver.find_element_by_xpath('//button[contains(text(),"Login")]')
        self.createaccount=self.driver.find_element_by_xpath('//a[@href="/Registration/"]')
