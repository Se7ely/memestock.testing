from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage

class ThreadsPage(MainPage):

    url = {'home': '/Home/', 'popular': '/popular/', 'all': '/All/', 'hot': '/Hot/'}

    def __init__(self, driver):
        MainPage.__init__(self,driver)

    # Await completion when multipe threads or database are available