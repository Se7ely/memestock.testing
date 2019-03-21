from GeneralUtilities import BrowserFunctions

driver=BrowserFunctions.BrowserLoad('chrome','https://www.reddit.com')
driver1=BrowserFunctions.BrowserLoad('googlechrome','https://www.reddit.com')
driver2=BrowserFunctions.BrowserLoad('adfsgfdh','https://www.reddit.com')
driver.close()
driver1.close()
driver2.close()



