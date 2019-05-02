from Pages.AccountSettingsPage import AccountSettingsPage
from GeneralUtilities import BrowserFunctions


class AccountSettingsPageEmail(AccountSettingsPage):

    def __init__(self):
        self.updateemail= '//input[@type="email"]'
        self.updateemailbutton= '//input[@type="submit"]'


    def GetUpdateEmailButton(self, driver):
        return driver.find_element_by_xpath(self.updateemailbutton)

    def GetUpdateEmail(self, driver):
        return driver.find_element_by_xpath(self.updateemail)

