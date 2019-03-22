from Pages.UserSettingsPage import UserSettingsPage

class ProfileSettingsPage(UserSettingsPage):

    url='http://localhost:3000/Settings/Profile'

    def __init__(self,driver):
        UserSettingsPage.__init__(driver)
        self.displaynamefield = self.driver.find_element_by_xpath('//input[@placeholder="Display Name (optional)"]')
        self.biofield = self.driver.find_element_by_xpath('//textarea[@placeholder="About (optional)"]')