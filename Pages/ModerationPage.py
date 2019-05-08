from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage

class ModerationPage(MainPage):


    def __init__(self):
        MainPage.__init__(self)
        self.url='/moderation/'
        self.moderators='//a[@href ="/moderation/Moderators"]'
        self.moderationqueue='//a[@href ="/moderation/ModerationQueue"]'
        self.banusers='//a[@href ="/moderation/BanUsers"]'


    def GetModerator(self, driver):
        return driver.find_element_by_xpath(self.moderators)

    def GetModerationQueue(self, driver):
        return driver.find_element_by_xpath(self.moderationqueue)

    def GetBanUsers(self, driver):
        return driver.find_element_by_xpath(self.banusers)




