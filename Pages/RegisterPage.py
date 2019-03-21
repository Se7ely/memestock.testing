from selenium import webdriver
from GeneralUtilities import BrowserFunctions


class RegisterPage():
    url='http://localhost:3000/'

    def __init__(self,browser):
        self.driver=BrowserFunctions.BrowserLoad(browser,self.url)
        self.emailfield=self.driver.find_element_by_xpath('//input[@placeholder="E-mail"]')
        self.usernamefield=self.driver.find_element_by_xpath('//input[@placeholder="User name"]')
        self.passwordfield=self.driver.find_element_by_xpath('//input[@placeholder="Password"]')
        self.registerbutton=self.driver.find_element_by_xpath('//button[contains(text(),"Register")]')


