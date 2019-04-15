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



    def Redirect(self,driver):

        mp=MainPage()
        mp.Redirect(driver)
        mp.Getcreatepostbutton(driver).click()
        return

    def Getsubredditfield(self,driver):
        return driver.find_element_by_xpath(self.subredditfield)

    def Getcreatebutton(self,driver):
        return driver.find_element_by_xpath(self.createbutton)

    def Gettitlefield(self,driver):
        return driver.find_element_by_xpath(self.titlefield)

    def Getbodyfield(self,driver):
        return driver.find_element_by_xpath(self.bodyfield)
