from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage

class ThreadsPage(MainPage):

    def __init__(self,driver):
        super.__init__(driver)