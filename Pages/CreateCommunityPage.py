from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage

class CreateCommunityPage(MainPage):


    def __init__(self):
        MainPage.__init__(self)
        self.url = '/create-subreddit/'
        self.subredditnamefield='//input[@id="srSubredditName"]'
        self.subredditrulefields=['//textarea[@id="srSubredditRule1"]','//textarea[@id="srSubredditRule2"]','//textarea[@id="srSubredditRule3"]']
        self.subredditbio='//textarea[@id="srSubredditBio"]'
        self.subredditmoderator='//textarea[@id="srSubredditModerator"]'
        self.subredditcoverbutton='//label[@class="srSubredditPageCreateButton"]'
        self.createbutton='//button[@class="srSubredditPageCreateButton"]'

    def GetSubRedditNameField(self,driver):
        return driver.find_element_by_xpath(self.subredditnamefield)

    def GetSubRedditRuleFields(self,driver):
        return driver.find_element_by_xpath(self.subredditrulefields)

    def GetSubRedditBio(self,driver):
        return driver.find_element_by_xpath(self.subredditbio)

    def GetSubRedditModerator(self,driver):
        return driver.find_element_by_xpath(self.subredditmoderator)

    def GetSubRedditCoverButton(self,driver):
        return driver.find_element_by_xpath(self.subredditcoverbutton)

    def GetSubRedditCreateButton(self,driver):
        return driver.find_element_by_xpath(self.createbutton)

