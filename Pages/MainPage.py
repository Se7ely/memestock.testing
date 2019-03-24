from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.Page import Page
class MainPage(Page):

    def __init__(self,):

        Page.__init__(self)
        self.url='/Home/'
        self.totopanchor='//a[@href="#top"]'
        self.logobutton='//a[text()="Memestock"]'

        self.listingsdrop='//button[text()="Dropdown"]'
        self.normallisting='//a[text()="Home"]'
        self.popularlisting ='//a[text()="Popular"]'
        self.alllisting = '//a[text()="All"]'
        self.hotlisting ='//a[text()="Hot"]'

        self.searchbar='//input[@class="memeSearch"]'
        self.pmbutton ='//a[@href="/PM/"]'
        self.createpostbutton='//a[@href="/CreatePost/"]'
        self.notificationsbutton='//a[text()="Notifications"]'#expect change due to ambigious functionality

        self.yourstuffdrop='//button[text()="YOUR STUFF"]'
        self.myprofile='//a[@href="/My profile/"]'
        self.usersettings='//a[@href="/Settings/"]'

