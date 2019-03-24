from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage

class CreatePostPage(MainPage):


    def __init__(self):
        MainPage.__init__(self)
        self.url = '/CreatePost/'
