from Pages.SettingsPage import SettingsPage
from GeneralUtilities import BrowserFunctions
class ProfileSettingsPage(SettingsPage):


    def __init__(self):
        SettingsPage.__init__(self)
        self.url='/Settings/Profile'
        self.displaynamefield = '//input[@placeholder="Display Name (optional)"]'
        self.biofield = '//textarea[@placeholder="About (optional)"]'
        self.savebutton='//input[@id="submit"]'

    def Getdisplaynamefield(self, driver):
        return driver.find_element_by_xpath(self.displaynamefield)

    def Getbiofield(self, driver):
        return driver.find_element_by_xpath(self.biofield)

    def GetSaveButton(self, driver):
        return driver.find_element_by_xpath(self.savebutton)