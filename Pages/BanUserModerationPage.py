from Pages.ModerationPage import ModerationPage
from GeneralUtilities import BrowserFunctions
class BanUserModerationPage(ModerationPage):


    def __init__(self):
        ModerationPage.__init__(self)
        self.url='/moderation/BanUsers'
        self.selectuserban= '//div[@class ="css-1hwfws3"]'
        self.getuserban= '//input[@id ="getUserBan"]'
        self.donebutton='//input[@class ="saveComment"]'
        self.banuserscheckbox='//label[@class ="BanU"]'
        self.unbanuserscheckbox='//label[@class ="UnBanU"]'

    def GetSelectUserBan(self, driver):
        return driver.find_element_by_xpath(self.selectuserban)

    def GetGetUserBanself(self, driver):
        return driver.find_element_by_xpath(self.getuserban)

    def GetDoneButton(self, driver):
        return driver.find_element_by_xpath(self.donebutton)

    def GetBanUserCheckBox(self, driver):
        return driver.find_element_by_xpath(self.banuserscheckbox)

    def GetUnBanUserCheckBox(self, driver):
        return driver.find_element_by_xpath(self.unbanuserscheckbox)