from Pages.ModerationPage import ModerationPage
from GeneralUtilities import BrowserFunctions
class InviteModeratorsModerationPage(ModerationPage):


    def __init__(self):
        ModerationPage.__init__(self)
        self.url='/moderation/Moderators'
        self.select= '//div[@class ="css-1hwfws3"]'
        self.getuser= '//input[@id ="getUser"]'
        self.invitebutton='//input[@class ="saveComment"]'


    def GetSelect(self, driver):
        return driver.find_element_by_xpath(self.select)

    def GetGetUser(self, driver):
        return driver.find_element_by_xpath(self.getuser)

    def GetInviteButton(self, driver):
        return driver.find_element_by_xpath(self.invitebutton)