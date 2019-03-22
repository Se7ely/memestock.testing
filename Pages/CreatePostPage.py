from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage

class CreatePostPage(MainPage):

    url='http://localhost:3000/CreatePost/'

    def __init__(self,driver):
        MainPage.__init__(driver)