from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.Page import Page
from Pages.RegisterPage import RegisterPage # just to write redirect

class LoginPage(Page):

    def __init__(self):
        Page.__init__(self)
        self.url='/Login/'
        self.usernamefield='//input[@placeholder="User name"]'
        self.passwordfield='//input[@placeholder="Password"]'
        self.loginbutton='//button[contains(text(),"Login")]'
        self.createaccount='//a[@href="/Registration/"]'

    def Getusernamefield(self, driver):
        return driver.find_element_by_xpath(self.usernamefield)

    def Getpasswordfield(self,driver):
        return driver.find_element_by_xpath(self.passwordfield)

    def Getloginbutton(self,driver):
        return driver.find_element_by_xpath(self.loginbutton)

    def ErrorDisplayed(self,driver):
        error=driver.find_elements_by_xpath('//*[@class="Login_Invalid__3998w"]')
        return len(error)>0

    def Redirect(self,driver):#this is completely wrong it is just a method to overcome shorthandness in react routing
        rp=RegisterPage()
        rp.Getalreadyregistered(driver).click()



