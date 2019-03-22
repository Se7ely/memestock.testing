from selenium import webdriver
from GeneralUtilities import BrowserFunctions

class MainPage():

    def __init__(self,driver):

        self.driver=driver

        self.totopanchor=self.driver.find_element_by_xpath('//a[@href="#top"]')
        self.logobutton=self.driver.find_element_by_xpath('//a[text()="Memestock"]')

        self.listingsdrop=self.driver.find_element_by_xpath('//button[text()="Dropdown"]')
        self.normallisting=self.driver.find_element_by_xpath('//a[text()="Home"]')
        self.popularlisting = self.driver.find_element_by_xpath('//a[text()="Popular"]')
        self.alllisting = self.driver.find_element_by_xpath('//a[text()="All"]')
        self.hotlisting = self.driver.find_element_by_xpath('//a[text()="Hot"]')

        self.searchbar=self.driver.find_element_by_xpath('//input[@class="memeSearch"]')
        self.pmbutton = self.driver.find_element_by_xpath('//a[@href="/PM/"]')
        self.createpostbutton= self.driver.find_element_by_xpath('//a[@href="/CreatePost/"]')
        self.notificationsbutton= self.driver.find_element_by_xpath('//a[text()="Notifications"]')#expect change due to ambigious functionality

        self.yourstuffdrop= self.driver.find_element_by_xpath('//button[text()="YOUR STUFF"]')
        self.myprofile=self.driver.find_element_by_xpath('//a[@href="/My profile/"]')
        self.usersettings=self.driver.find_element_by_xpath('//a[@href="/Settings/"]')

