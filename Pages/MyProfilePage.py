from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage

class MyProfilePage(MainPage):


    def __init__(self):
        MainPage.__init__(self)
        self.url='/user/'
        self.overviewed='//a[@href="/user/"]'
        self.posts='//a[@href="/user/posts"]'
        self.comments='//a[@href="/user/comments"]'
        self.saved='//a[@href="/user/saved"]'
        self.hidden='//a[@href="/user/hidden"]'
        self.profilename='//div[@class="stuff"]'

    def GetOverViewedButton(self, driver):
        return driver.find_element_by_xpath(self.overviewed)

    def GetPostsButton(self, driver):
        return driver.find_element_by_xpath(self.posts)

    def GetCommentsButton(self, driver):
        return driver.find_element_by_xpath(self.comments)

    def GetSavedButton(self, driver):
        return driver.find_element_by_xpath(self.saved)

    def GetHiddenButton(self, driver):
        return driver.find_element_by_xpath(self.hidden)

    def GetProfilename(self, driver):
        return driver.find_element_by_xpath(self.profilename)


