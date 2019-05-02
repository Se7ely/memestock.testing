from Pages.AccountSettingsPage import AccountSettingsPage
from GeneralUtilities import BrowserFunctions


class AccountSettingsPagePassword(AccountSettingsPage):

    def __init__(self):

        self.oldpassword= '//input[@id="oldPassword"]'
        self.newpassword= '//input[@id="newPassword"]'
        self.subbutton= '//input[@id="submit"]'



    def GetSubButton(self, driver):
        return driver.find_element_by_xpath(self.subbutton)

    def GetOldPassword(self, driver):
        return driver.find_element_by_xpath(self.oldpassword)

    def GetNewPassword(self, driver):
        return driver.find_element_by_xpath(self.newpassword)