from selenium import webdriver
import os

class BrowserClose:

    def __init__(self, driver):
        self.driver = driver

    def BClose(self):
        self.driver.close()


