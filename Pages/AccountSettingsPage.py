from Pages.SettingsPage import SettingsPage
from GeneralUtilities import BrowserFunctions
class AccountSettingsPage(SettingsPage):

    def __init__(self):
        SettingsPage.__init__(self)
        self.url = '/Settings/Account'
        self.changeorupdateemail='//a[text()="Change/add Email"]'
        self.changepassword ='//a[text()="Change Password"]'

        self.oldpassword= '//input[@id="oldPassword"]'
        self.newpassword= '//input[@id="newPassword"]'
        self.subbutton= '//input[@id="submit"]'

    def GetChangeOrUpdateEmail(self, driver):
        return driver.find_element_by_xpath(self.changeorupdateemail)

    def GetChangePassword(self, driver):
        return driver.find_element_by_xpath(self.changepassword)


