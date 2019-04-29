from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.Page import Page
class MainPage(Page):

    def __init__(self):

        Page.__init__(self)
        self.url=''
        self.totopanchor='//a[@href="#top"]'
        self.logobutton='//div[@class="memeLogo"]'

        self.contentdrop='//div[@class="dropList"]//preceding-sibling::button'
        self.homecontent='//div[@class="dropList"]//span[text()="Home"]'
        self.popularcontent ='//div[@class="dropList"]//span[text()="Popular"]'
        self.allcontent = '//div[@class="dropList"]//span[text()="All"]'
        self.hotcontent ='//div[@class="dropList"]//span[text()="Hot"]'

        self.searchbar='//input[@id="header-search-bar"]'
        self.pmbutton ='//a[@href="/PM/"]'
        self.createpostbutton='//a[@href="/CreatePost/"]'
        self.notificationsbutton='//a[@href="#"]'#expect change due to ambigious functionality
        self.loginform='//button[text()="Log In"]'
        self.signupform='//button[text()="Sign Up"]'

        self.usernamefieldli='//input[@class="usernameInput logi"]'
        self.passwordfieldli='//input[@class="passInput logi"]'
        self.loginbutton='//button[text()=" Login "]'

        self.emailfieldsu='//input[@class="emailInput in"]'
        self.usernamefieldsu='//input[@class="usernameInput in"]'
        self.passwordfieldsu='//input[@class="passInput in"]'
        self.signupbutton='//button[text()="SIGN UP"]'

        self.yourstuffdrop='//div[@class="yourStuffDropList"]//preceding-sibling::button' # wait till login to verify
        self.myprofile='//span[@to="/user/"]'
        self.usersettings='//span[@to="/settings/"]'
        self.logout='//a[@href="#logout"]'

        self.createpostfloating='//button[text()="Create Post"]'
        self.createcoummunityfloating='//button[text()=" Create Community"]'



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

    def Getusersettings(self,driver):
        return driver.find_element_by_xpath(self.usersettings)

    def GetMyProfile(self,driver):
        return driver.find_element_by_xpath(self.myprofile)








