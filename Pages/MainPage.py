from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.Page import Page
class MainPage(Page):

    def __init__(self):

        Page.__init__(self)
        self.url='/'
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
        self.logininvalid='//p[@class="Login_Invalid__3998w"]'

        self.emailfieldsu='//input[@class="emailInput in"]'
        self.usernamefieldsu='//input[@class="usernameInput in"]'
        self.passwordfieldsu='//input[@class="passInput in"]'
        self.signupbutton='//button[text()="SIGN UP"]'
        self.signupinvalid='//p[@class="Registration_Invalid__3zjtz"]'

        self.yourstuffdrop='//div[@class="yourStuffDropList"]//preceding-sibling::button' # wait till login to verify
        self.myprofile='//span[@to="/user/"]'
        self.usersettings='//span[@to="/settings/"]'
        self.logout='//a[@href="#logout"]'

        self.createpostfloating='//button[text()="Create Post"]'
        self.createcoummunityfloating='//button[text()=" Create Community"]'




    def GetTotoPanchor(self, driver):
        return driver.find_element_by_xpath(self.totopanchor)

    def GetLogoButton(self, driver):
        return driver.find_element_by_xpath(self.logobutton)

    def GetSearchBar(self, driver):
        return driver.find_element_by_xpath(self.searchbar)

    def GetPmButton(self, driver):
        return driver.find_element_by_xpath(self.pmbutton)

    def GetCreatePostButton(self, driver):
        return driver.find_element_by_xpath(self.createpostbutton)

    def GetNotificationsButton(self, driver):
        return driver.find_element_by_xpath(self.notificationsbutton)

    def GetYourStuffDrop(self, driver):
        return driver.find_element_by_xpath(self.yourstuffdrop)

    def GetUserSettings(self, driver):
        return driver.find_element_by_xpath(self.usersettings)

    def GetMyProfile(self,driver):
        return driver.find_element_by_xpath(self.myprofile)

    def GetLoginFormButton(self,driver):
        return driver.find_element_by_xpath(self.loginform)

    def GetUsernameLoginField(self,driver):
        return driver.find_element_by_xpath(self.usernamefieldli)

    def GetPasswordLoginField(self,driver):
        return driver.find_element_by_xpath(self.passwordfieldli)

    def GetLoginButtonField(self,driver):
        return driver.find_element_by_xpath(self.loginbutton)

    def GetSignupFormButton(self,driver):
        return driver.find_element_by_xpath(self.signupform)

    def GetUsernameSignupField(self,driver):
        return driver.find_element_by_xpath(self.usernamefieldsu)

    def GetEmailSignupField(self,driver):
        return driver.find_element_by_xpath(self.emailfieldsu)

    def GetPasswordSignupField(self,driver):
        return driver.find_element_by_xpath(self.passwordfieldsu)

    def GetSignupButton(self,driver):
        return driver.find_element_by_xpath(self.signupbutton)

    def Login(self,driver,username,password):
        self.GetUsernameLoginField(driver).send_keys(username)
        self.GetPasswordLoginField(driver).send_keys(password)
        self.GetLoginButtonField(driver).click()
        return

    def LoggedIn(self,driver):
        l=driver.find_elements_by_xpath(self.yourstuffdrop)
        return len(l)!=0

    def LoginErrorIsOn(self, driver):
        l=driver.find_elements_by_xpath(self.logininvalid)
        return len(l) != 0

    def SignupErrorIsOn(self,driver):
        l = driver.find_elements_by_xpath(self.signupinvalid)
        return len(l) != 0


    def Signup(self,driver,username,email,password):
        self.GetUsernameSignupField(driver).send_keys(username)
        self.GetEmailSignupField(driver).send_keys(email)
        self.GetPasswordSignupField(driver).send_keys(password)
        self.GetSignupButton(driver).click()











