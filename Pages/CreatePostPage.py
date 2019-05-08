from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage

class CreatePostPage(MainPage):


    def __init__(self):
        MainPage.__init__(self)
        self.url = '/CreatePost/'
        self.subredditfield='//input[@id="threadPageSubredditNameField"]'
        self.titlefield='//textarea[@id="threadPageTitleField"]'
        self.bodyfield='//textarea[@id="threadPageBodyField"]'
        self.createbutton='//button[@class="threadPageCreateButton"]'
        self.spoilercheckbox='//input[@name="Spoiler"]'
        self.photobutton='//label[@class="threadPageCreateButton"]'

    def GetSubRedditField(self, driver):
        return driver.find_element_by_xpath(self.subredditfield)

    def GetCreateButton(self, driver):
        return driver.find_element_by_xpath(self.createbutton)

    def GetTitleField(self, driver):
        return driver.find_element_by_xpath(self.titlefield)

    def GetBodyField(self, driver):
        return driver.find_element_by_xpath(self.bodyfield)

    def GetPhotoButton(self, driver):
        return driver.find_element_by_xpath(self.photobutton)

    def GetSpoilerCheckBox(self, driver):
        return driver.find_element_by_xpath(self.spoilercheckbox)
