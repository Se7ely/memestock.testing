from Pages.PMPage import PMPage
from GeneralUtilities import BrowserFunctions


class PMSentPage(PMPage):


    def __init__(self):
        PMPage.__init__(self)
        self.url='/Sent'

