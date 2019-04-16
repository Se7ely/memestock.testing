from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.Page import Page


class RegisterPage(Page):


    def __init__(self):
        Page.__init__(self)
        self.url='/Registration/'
        self.emailfield='//input[@placeholder="E-mail"]'
        self.usernamefield='//input[@placeholder="User name"]'
        self.passwordfield='//input[@placeholder="Password"]'
        self.registerbutton='//button[@class="registerButton"]'
        self.alreadyregistered='//a[@href="/Login/"]'

    def ErrorDisplayed(self,driver):
        error=driver.find_elements_by_xpath('//*[@class="Registration_Invalid__3zjtz"]')
        return len(error)>0
    def Getpasswordfield(self,driver):
        return driver.find_element_by_xpath(self.passwordfield)

    def GetRegisterbutton(self,driver):
        return driver.find_element_by_xpath(self.registerbutton)

    def Getusernamefield(self,driver):
        return driver.find_element_by_xpath(self.usernamefield)

    def Getemailfield(self,driver):
        return driver.find_element_by_xpath(self.emailfield)

    def Getalreadyregistered(self,driver):
        return driver.find_element_by_xpath(self.alreadyregistered)



