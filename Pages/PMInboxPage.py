from Pages.PMPage import PMPage
from GeneralUtilities import BrowserFunctions


class PMInboxPage(PMPage):


    def __init__(self):
        PMPage.__init__(self)
        self.markreadbutton='//button[@name="markRead"]'
        self.markunreadbutton='//button[@name="markunRead"]'
        self.blocklistbutton='//button[@name="blockList"]'

    def GetMarkReadButton(self,driver):
        return driver.find_element_by_xpath(self.markreadbutton)

    def GetMarkUnreadButton(self,driver):
        return driver.find_element_by_xpath(self.markunreadbutton)

    def GetBlocklist(self,driver):
        return driver.find_element_by_xpath(self.blocklistbutton)