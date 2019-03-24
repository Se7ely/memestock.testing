from GeneralUtilities import BrowserFunctions
from Pages.RegisterPage import RegisterPage
from Pages.MainPage import MainPage
import unittest, pytest
from ddt import ddt, data, unpack


@pytest.fixture()
def Setup():
    """ create tester object """
    # how to use the list below for arg?

    driver=BrowserFunctions.BrowserLoad()

    yield driver
    driver.close()

@pytest.mark.usefixtures('Setup')
class TestRegistration():

    def test_ValidRegistration(self,Setup):

        rp=RegisterPage()
        rp.Getpasswordfield(Setup).send_keys('s2sghjgksdfg')
        rp.GetRegisterbutton(Setup).click()
        mp=MainPage()
        print(Setup.current_url)

        assert mp.IsOn(Setup)

    def test_InvalidRegistration(self,Setup):

        rp = RegisterPage()
        rp.Getpasswordfield(Setup).send_keys('1yre')
        rp.GetRegisterbutton(Setup).click()

        assert rp.ErrorDisplayed(Setup)


        """ 
    def CleanUp(self):
        self.driver.
        """


