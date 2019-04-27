from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage
from Pages.LoginPage import LoginPage
import unittest, pytest

@pytest.fixture()
def Setup():

    driver=BrowserFunctions.BrowserLoad()
    lp=LoginPage()
    lp.Redirect(driver)

    yield driver
    driver.close()



@pytest.mark.usefixtures('Setup')
class TestMultipageLogin():

    def test_RightUsernameDisplayed(self,Setup):
        lp=LoginPage()
        mp=MainPage()
        username="tester"
        password="1234567890"
        lp.Getusernamefield(Setup).send_keys(username)
        lp.Getpasswordfield(Setup).send_keys(password)
        lp.Getloginbutton(Setup).click()
        #remove refresh when frontend is better
        Setup.refresh()
        assert mp.GetUsernameDisplay(Setup).text==username