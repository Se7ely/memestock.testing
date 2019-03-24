from Pages.UserSettingsPage import UserSettingsPage
from GeneralUtilities import BrowserFunctions
class AccountSettingsPage(UserSettingsPage):

    url='/Settings/Account'

    def __init__(self):
        UserSettingsPage.__init__(self)
        self.url = '/Settings/Account'
        self.email='//a[text()="Change/add Email"]'
        self.password ='//a[text()="Change Password"]'