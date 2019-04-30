from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage
import unittest, pytest

from ddt import ddt, data, unpack


@pytest.fixture()
def Setup():

    driver=BrowserFunctions.BrowserLoad()
    mp=MainPage()
    mp.Redirect(driver)
    mp.GetLoginFormButton(driver).click()
    yield driver
    driver.close()

@pytest.mark.usefixtures('Setup')
class TestLogin():

    def test_LoginSuccesful(self,Setup):

        mp=MainPage()
        mp.Login(Setup,'repeateduser','1234567890')
        assert mp.LoggedIn(Setup)

    def test_LoginFailedInvalidPassword(self,Setup):

        mp = MainPage()
        mp.Login(Setup, 'repeateduser', '1yre')
        assert mp.LoginErrorIsOn(Setup)

    def test_LoginFailedIncorrectPassword(self,Setup):

        mp = MainPage()
        mp.Login(Setup, 'repeateduser', '1231234246732')
        assert mp.LoginErrorIsOn(Setup)

    def test_LoginFailedIncorrectUsername(self, Setup):

        mp = MainPage()
        mp.Login(Setup, 'nulluser', '12345678')
        assert mp.LoginErrorIsOn(Setup)


    def test_Refresh(self,Setup):
        mp=MainPage()
        Setup.refresh()
        assert mp.IsOn(Setup)
        #add assert checking content is still on page




