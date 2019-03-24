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
        self.registerbutton='//button[contains(text(),"Register")]'
        self.alreadyregistered='//a[@href="/Login/"]'

    def ErrorDisplayed(self,driver):
        error=driver.find_elements_by_xpath('//p[@class="Registration_Invalid__3zjtz"]')
        return len(error)>0
    def Getpasswordfield(self,driver):
        return driver.find_element_by_xpath(self.passwordfield)

    def GetRegisterbutton(self,driver):
        return driver.find_element_by_xpath(self.registerbutton)


