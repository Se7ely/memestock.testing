from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage

class PMPage(MainPage):

    url='http://localhost:3000/PM/'

    def __init__(self,driver):
        MainPage.__init__(driver)