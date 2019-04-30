from Pages.AccountSettingsPage import AccountSettingsPage
from GeneralUtilities import BrowserFunctions


class AccountSettingsPageEmail(AccountSettingsPage):

    def __init__(self):
        self.updateEmail='//input[@type="email"]'
        self.updateEmailButton='//input[@type="submit"]'


    def Getpupdatemailbutton(self,driver):
        return driver.find_element_by_xpath(self.updateEmailButton)

    def GetupdateEmail(self,driver):
        return driver.find_element_by_xpath(self.updateEmail)

