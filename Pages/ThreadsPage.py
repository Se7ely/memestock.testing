from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.PageElements.Threads import Thread
from Pages.MainPage import MainPage

class ThreadsPage(MainPage):


    def __init__(self):
        MainPage.__init__(self)
        self.url= {'home': '/Home/', 'popular': '/popular/', 'all': '/All/', 'hot': '/Hot/'}

    def GetThreads(self,driver):
        threadslist=[]
        for i in range(len(driver.find_elements_by_xpath(self.threads))):
            threadslist.append(Thread(i+1))

        return threadslist