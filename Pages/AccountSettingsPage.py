from Pages.UserSettingsPage import UserSettingsPage
from GeneralUtilities import BrowserFunctions
class AccountSettingsPage(UserSettingsPage):

    url='/Settings/Account'

    def __init__(self):
        UserSettingsPage.__init__(self)
        self.url = '/Settings/Account'
        self.changeorupdateemail='//a[text()="Change/add Email"]'
        self.changepassword ='//a[text()="Change Password"]'
        self.updateEmail='//input[@type="email"]'
        self.updateEmailButton='//input[@type="submit"]'
        self.oldPassword='//input[@id="oldPassword"]'
        self.newPassword='//input[@id="newPassword"]'
        self.subButton='//input[@id="submit"]'

    def Getchangeorupdateemail(self,driver):
        return driver.find_element_by_xpath(self.changeorupdateemail)

    def Getchangepassword(self,driver):
        return driver.find_element_by_xpath(self.changepassword)

    def GetupdateEmail(self,driver):
        return driver.find_element_by_xpath(self.updateEmail)

    def Getpupdatemailbutton(self,driver):
        return driver.find_element_by_xpath(self.updateEmailButton)

    def Getsubbutton(self,driver):
        return driver.find_element_by_xpath(self.subButton)

    def Getoldpassword(self,driver):
        return driver.find_element_by_xpath(self.oldPassword)

    def Getnewpassword(self,driver):
        return driver.find_element_by_xpath(self.newPassword)

    def Redirect(self,driver):
        us=UserSettingsPage()
        us.Redirect(driver)
        us.Getaccounttab(driver).click()
        return