from selenium import webdriver
from GeneralUtilities import BrowserFunctions

class MainPage():
    url='http://localhost:3000/home'

    def __init__(self,driver):

        self.driver=driver

        self.totopanchor=self.driver.find_element_by_xpath('//a[@href="#top"]')
        self.logobutton=self.driver.find_element_by_xpath('//a[text()="Memestock"]')
        self.listingsdrop=self.driver.find_element_by_xpath('//button[text()="Dropdown"]')
        self.searchbar=self.driver.find_element_by_xpath('//input[@class="memeSearch"]')
        self.pmbutton = self.driver.find_element_by_xpath('//a[@href="/PM/"]')
        self.createpostbutton= self.driver.find_element_by_xpath('//a[@href="/CreatePost/"]')
        self.notificationsbutton= self.driver.find_element_by_xpath('//a[text()="Notifications"]')#expect change due to ambigious functionality
        self.yourstuffdrop= self.driver.find_element_by_xpath('//button[text()="YOUR STUFF"]')
