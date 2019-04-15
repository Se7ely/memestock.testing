from Pages.UserSettingsPage import UserSettingsPage
from GeneralUtilities import BrowserFunctions
class ProfileSettingsPage(UserSettingsPage):



    def __init__(self):
        UserSettingsPage.__init__(self)
        self.url='/Settings/Profile'
        self.displaynamefield = '//input[@placeholder="Display Name (optional)"]'
        self.biofield = '//textarea[@placeholder="About (optional)"]'

    def Getdisplaynamefield(self, driver):
        return driver.find_element_by_xpath(self.displaynamefield)

    def Getbiofield(self, driver):
        return driver.find_element_by_xpath(self.biofield)

    def Redirect(self,driver):
        us=UserSettingsPage()
        us.Redirect(driver)
        us.Getprofiletab(driver).click()
        return