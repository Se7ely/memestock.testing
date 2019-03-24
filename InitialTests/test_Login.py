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

    def test_ValidLogin(self,Setup):

        lp=LoginPage()
        lp.Getpasswordfield(Setup).send_keys('s2sghjgksdfg')
        lp.Getloginbutton(Setup).click()
        mp=MainPage()

        assert mp.IsOn(Setup)

    def test_InvalidLogin(self,Setup):

        lp = LoginPage()
        lp.Getpasswordfield(Setup).send_keys('1yre')
        lp.Getloginbutton(Setup).click()

        assert lp.ErrorDisplayed(Setup)


        """ 
    def CleanUp(self):
        self.driver.
        """