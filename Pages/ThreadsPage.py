from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.PageElements.Threads import Thread
from Pages.MainPage import MainPage

class ThreadsPage(MainPage):


    def __init__(self):
        MainPage.__init__(self)
        self.url=['/Home/','/popular/','/Hot/']

        self.threads='//div[@class="threadContainer"]'

    def GetThreads(self,driver):
        threadslist=[]
        for i in range(len(driver.find_elements_by_xpath(self.threads))):
            threadslist.append(Thread(i+1))

        return threadslist

    def IsOn(self,driver):
        res=False
        for i in self.url:
            if BrowserFunctions.baseurl+i==driver.current_url:
                res=True
                break

        return res
