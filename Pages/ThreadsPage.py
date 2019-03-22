from selenium import webdriver
from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage

class ThreadsPage(MainPage):

    url={'home':'http://localhost:3000/Home/','popular':'http://localhost:3000/popular/',
         'all':'http://localhost:3000/All/','hot':'http://localhost:3000/Hot/'}

    def __init__(self,driver):
        MainPage.__init__(driver)

    #Await completion when multipe threads or database are available