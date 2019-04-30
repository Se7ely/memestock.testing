from Pages.AccountSettingsPage import AccountSettingsPage
from GeneralUtilities import BrowserFunctions


class AccountSettingsPagePassword(AccountSettingsPage):

    def __init__(self):

        self.oldPassword='//input[@id="oldPassword"]'
        self.newPassword='//input[@id="newPassword"]'
        self.subButton='//input[@id="submit"]'



    def Getsubbutton(self,driver):
        return driver.find_element_by_xpath(self.subButton)

    def Getoldpassword(self,driver):
        return driver.find_element_by_xpath(self.oldPassword)

    def Getnewpassword(self,driver):
        return driver.find_element_by_xpath(self.newPassword)