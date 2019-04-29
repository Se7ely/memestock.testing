from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage

class CreateCommunityPage(MainPage):


    def __init__(self):
        MainPage.__init__(self)
        self.url = '/create-subreddit/'
        self.subredditnamefield='//input[@id="srSubredditName"]'
        self.subredditrulefields=['//textarea[@id="srSubredditRule1"]','//textarea[@id="srSubredditRule2"]','//textarea[@id="srSubredditRule3"]']
        self.createbutton='//button[@class="srSubredditPageCreateButton"]'




