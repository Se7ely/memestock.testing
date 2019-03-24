from Pages.RegisterPage import RegisterPage
from Pages.MainPage import MainPage
import time
from selenium.webdriver.common.keys import Keys
from GeneralUtilities import BrowserFunctions


driver=BrowserFunctions.BrowserLoad('chrome')
rp=RegisterPage(driver)
rp.emailfield.send_keys('is it working ??')
rp.emailfield.clear()
rp.usernamefield.send_keys('goodddaaaamnnn')
rp.passwordfield.send_keys('assdfgfbdfgsd')
rp.registerbutton.click()

mp=MainPage(driver)

mp.listingsdrop.click()
mp.createpostbutton.click()
# mp.pmbutton.click(mp.logobutton.click()
mp.notificationsbutton.click()
mp.searchbar.send_keys('ok ?')
time.sleep(3)
mp.searchbar.clear()
mp.logobutton.click()
print(str(mp.IsOn()))
mp.searchbar.send_keys(Keys.ENTER)

mp.driver.close()



