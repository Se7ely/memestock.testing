from GeneralUtilities import BrowserFunctions
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
import unittest, pytest

from ddt import ddt, data, unpack


@pytest.fixture()
def Setup():

    driver=BrowserFunctions.BrowserLoad()
    lp=LoginPage()
    lp.Redirect(driver)
    yield driver
    driver.close()

@pytest.mark.usefixtures('Setup')
class TestLogin():

    def test_LoginSuccesful(self,Setup):

        lp=LoginPage()
        lp.Getusernamefield(Setup).send_keys('mostafa_hazem')
        lp.Getpasswordfield(Setup).send_keys('12345678')
        lp.Getloginbutton(Setup).click()
        mp=MainPage()
        assert mp.IsOn(Setup)

    def test_LoginFailedInvalidPassword(self,Setup):

        lp = LoginPage()
        lp.Getusernamefield(Setup).send_keys('mostafa_hazem')
        lp.Getpasswordfield(Setup).send_keys('1yre')
        lp.Getloginbutton(Setup).click()

        assert lp.ErrorDisplayed(Setup)

    def test_LoginFailedIncorrectPassword(self,Setup):

        lp = LoginPage()
        lp.Getusernamefield(Setup).send_keys('mostafa_hazem')
        lp.Getpasswordfield(Setup).send_keys('1231234246732')
        lp.Getloginbutton(Setup).click()
        assert lp.ErrorDisplayed(Setup)

    def test_LoginFailedIncorrectUsername(self, Setup):
        lp = LoginPage()
        lp.Getusernamefield(Setup).send_keys('Mostafa.Hazem')
        lp.Getpasswordfield(Setup).send_keys('12345678')
        lp.Getloginbutton(Setup).click()

        assert lp.ErrorDisplayed(Setup)

    def test_Refresh(self,Setup):
        lp=LoginPage()
        Setup.refresh()
        assert lp.IsOn(Setup)
        #add assert checking content is still on page




