from GeneralUtilities import BrowserFunctions
import Pages
from Pages.RegisterPage import RegisterPage
from Pages.MainPage import MainPage
from Pages.UserSettingsPage import UserSettingsPage
from Pages.AccountSettingsPage import AccountSettingsPage
from Pages.ProfileSettingsPage import ProfileSettingsPage
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys

driver=BrowserFunctions.BrowserLoad('gsfd')

rp=RegisterPage(driver)
rp.emailfield.send_keys('is it working ??')
rp.emailfield.clear()
rp.usernamefield.send_keys('goodddaaaamnnn')
rp.passwordfield.send_keys('assdfgfbdfgsd')
rp.registerbutton.click()

mp=MainPage(driver)
BrowserFunctions.Hover(mp.yourstuffdrop,driver)
mp.usersettings.click()

sp=UserSettingsPage(driver)
sp.accounttab.click()

print(driver.current_url)