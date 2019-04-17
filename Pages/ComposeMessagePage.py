from Pages.PMPage import PMPage
from GeneralUtilities import BrowserFunctions


class ComposeMessagePage(PMPage):


    def __init__(self):
        PMPage.__init__(self)
        self.url='/PM/Compose'
        self.To='//*[@id="1"]'
        self.Subject='//*[@id="2"]'
        self.Yourmessage='//*[@id="3"]'
        self.SubmitButton='//*[@id="root"]/div/div/div[4]/div/form/input'

    def GetToText(self, driver):
        return driver.find_element_by_xpath(self.To)

    def GetSubjectText(self, driver):
        return driver.find_element_by_xpath(self.Subject)

    def GetYourMessage(self, driver):
        return driver.find_element_by_xpath(self.Yourmessage)

    def GetSubmitButton(self, driver):
        return driver.find_element_by_xpath(self.SubmitButton)