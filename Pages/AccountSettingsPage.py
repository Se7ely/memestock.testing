from Pages.SettingsPage import SettingsPage
from GeneralUtilities import BrowserFunctions
class AccountSettingsPage(SettingsPage):

    def __init__(self):
        SettingsPage.__init__(self)
        self.url = '/Settings/Account'
        self.changeorupdateemail='//a[text()="Change/add Email"]'
        self.changepassword ='//a[text()="Change Password"]'

        self.oldPassword='//input[@id="oldPassword"]'
        self.newPassword='//input[@id="newPassword"]'
        self.subButton='//input[@id="submit"]'

    def Getchangeorupdateemail(self,driver):
        return driver.find_element_by_xpath(self.changeorupdateemail)

    def Getchangepassword(self,driver):
        return driver.find_element_by_xpath(self.changepassword)


