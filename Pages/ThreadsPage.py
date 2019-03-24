from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage

class ThreadsPage(MainPage):


    def __init__(self):
        MainPage.__init__(self)
        self.url= {'home': '/Home/', 'popular': '/popular/', 'all': '/All/', 'hot': '/Hot/'}

    # Await completion when multipe threads or database are available