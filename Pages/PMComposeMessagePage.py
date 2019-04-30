from Pages.PMPage import PMPage
from GeneralUtilities import BrowserFunctions


class PMComposeMessagePage(PMPage):


    def __init__(self):
        PMPage.__init__(self)
        self.url='/PM/Compose'
        self.tofield='//textarea[@id="1"]'
        self.subjectfield='//textarea[@id="2"]'
        self.messagefield='//textarea[@id="3"]'
        self.submitbutton='//input[@type="submit"]'

    def GetToField(self, driver):
        return driver.find_element_by_xpath(self.tofield)

    def GetSubjectField(self, driver):
        return driver.find_element_by_xpath(self.subjectfield)

    def GetMessageField(self, driver):
        return driver.find_element_by_xpath(self.messagefield)

    def GetSubmitButton(self, driver):
        return driver.find_element_by_xpath(self.submitbutton)