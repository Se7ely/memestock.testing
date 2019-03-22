from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage

class UserSettingsPage(MainPage):

    url='http://localhost:3000/Settings/'

    def __init__(self,driver):
        MainPage.__init__(driver)
        self.accounttab=self.driver.find_element_by_xpath('//a[@href="/Settings/Account"]')
        self.profiletab=self.driver.find_element_by_xpath('//a[@href="/Settings/Profile"]')