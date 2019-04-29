from Pages.AccountSettingsPage import AccountSettingsPage
from GeneralUtilities import BrowserFunctions


class AccountSettingsPagePassword(AccountSettingsPage):

    def __init__(self):

        self.oldPassword='//input[@id="oldPassword"]'
        self.newPassword='//input[@id="newPassword"]'
        self.subButton='//input[@id="submit"]'