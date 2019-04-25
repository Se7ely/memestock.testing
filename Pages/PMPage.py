from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage

class PMPage(MainPage):


    def __init__(self):
        MainPage.__init__(self)
        self.url='/PM/'
        self.messaging='//h1[text()="Messaging"]'
        self.composemessage='//a[@href="/PM/Compose"]'
        self.sent='//a[@href="/Sent"]'
        self.inbox='//a[@href="/Inbox"]'



    def GetMessaging(self, driver):
        return driver.find_element_by_xpath(self.messaging)

    def GetComposmessaging(self, driver):
        return driver.find_element_by_xpath(self.composemessage)

    def GetSent(self, driver):
        return driver.find_element_by_xpath(self.sent)

    def Getinbox(self, driver):
        return driver.find_element_by_xpath(self.inbox)

    def Redirect(self, driver):
        mp = MainPage()
        mp.Redirect(driver)
        mp.Getpmbutton(driver).click()
        return
