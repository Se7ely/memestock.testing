from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage

class PMPage(MainPage):


    def __init__(self):
        MainPage.__init__(self)
        self.url='/PM/'
        self.composemessage='//a[@href="/PM/Compose"]'
        self.sent='//a[@href="/Sent"]'
        self.inbox='//a[text()="Inbox"]'




    def GetComposeMessaging(self, driver):
        return driver.find_element_by_xpath(self.composemessage)

    def GetSent(self, driver):
        return driver.find_element_by_xpath(self.sent)

    def GetInbox(self, driver):
        return driver.find_element_by_xpath(self.inbox)


