from Pages.AccountSettingsPage import AccountSettingsPage
from GeneralUtilities import BrowserFunctions


class AccountSettingsPageEmail(AccountSettingsPage):

    def __init__(self):
        self.updateEmail='//input[@type="email"]'
        self.updateEmailButton='//input[@type="submit"]'
