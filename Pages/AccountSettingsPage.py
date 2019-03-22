from Pages.UserSettingsPage import UserSettingsPage

class AccountSettingsPage(UserSettingsPage):

    url='/Settings/Account'

    def __init__(self,driver):
        UserSettingsPage.__init__(self,driver)
        self.email=self.driver.find_element_by_xpath('//a[text()="Change/add Email"]')
        self.password = self.driver.find_element_by_xpath('//a[text()="Change Password"]')