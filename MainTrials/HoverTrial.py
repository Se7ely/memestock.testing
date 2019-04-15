from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage

driver=BrowserFunctions.BrowserLoad(BrowserFunctions.baseurl)
mp=MainPage()
mp.Redirect()
mp.