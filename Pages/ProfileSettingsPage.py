from Pages.UserSettingsPage import UserSettingsPage
from GeneralUtilities import BrowserFunctions
class ProfileSettingsPage(UserSettingsPage):



    def __init__(self,driver):
        UserSettingsPage.__init__(self)
        self.url='/Settings/Profile'
        self.displaynamefield = '//input[@placeholder="Display Name (optional)"]'
        self.biofield = '//textarea[@placeholder="About (optional)"]'