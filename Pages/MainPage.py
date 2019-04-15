from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.Page import Page
from Pages.LoginPage import LoginPage
from Pages.PageElements.Threads import Thread
class MainPage(Page):

    def __init__(self,):

        Page.__init__(self)
        self.url='/Home/'
        self.totopanchor='//a[@href="#top"]'
        self.logobutton='//div[@class="memeLogo"]/a[@href="/Home/"]'

        self.contentdrop='//div[@class="dropList"]//preceding-sibling::button'
        self.homecontent='//div[@class="dropList"]//a[@href="/Home/"]'
        self.popularcontent ='//div[@class="dropList"]//a[@href="/popular/"]'
        self.allcontent = '//div[@class="dropList"]//a[@href="/All/"]'
        self.hotcontent ='//div[@class="dropList"]//a[@href="/Hot/"]'

        self.searchbar='//input[@id="header-search-bar"]'
        self.pmbutton ='//a[@href="/PM/"]'
        self.createpostbutton='//a[@href="/CreatePost/"]'
        self.notificationsbutton='//a[text()="Notifications"]'#expect change due to ambigious functionality

        self.yourstuffdrop='//div[@class="yourStuffDropList"]//preceding-sibling::button'
        self.myprofile='//a[@href="/My profile/"]'
        self.usersettings='//a[@href="/Settings/"]'

        self.threads='//div[@class="threadContainer"]'

    def Redirect(self,driver):
        lp=LoginPage()
        lp.Redirect(driver)
        lp.Getusernamefield(driver).send_keys('mostafa_hazem')
        lp.Getpasswordfield(driver).send_keys('12345678')
        lp.Getloginbutton(driver).click()
        return

    def Gettotopanchor(self,driver):
        return driver.find_element_by_xpath(self.totopanchor)

    def Getlogobutton(self,driver):
        return driver.find_element_by_xpath(self.logobutton)

    def Getsearchbar(self,driver):
        return driver.find_element_by_xpath(self.searchbar)

    def Getpmbutton(self,driver):
        return driver.find_element_by_xpath(self.pmbutton)

    def Getcreatepostbutton(self,driver):
        return driver.find_element_by_xpath(self.createpostbutton)

    def Getnotificationsbutton(self,driver):
        return driver.find_element_by_xpath(self.notificationsbutton)

    def Getyourstuffdrop(self,driver):
        return driver.find_element_by_xpath(self.yourstuffdrop)

    def GetThreads(self,driver):
        threadslist=[]
        for i in range(len(driver.find_elements_by_xpath(self.threads))):
            threadslist.append(Thread(i+1))

        return threadslist






