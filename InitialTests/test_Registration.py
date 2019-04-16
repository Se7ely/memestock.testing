from GeneralUtilities import BrowserFunctions
from Pages.RegisterPage import RegisterPage
from Pages.MainPage import MainPage
import unittest, pytest
from ddt import ddt, data, unpack


@pytest.fixture()
def Setup():

    driver=BrowserFunctions.BrowserLoad()

    yield driver
    driver.close()

@pytest.mark.usefixtures('Setup')
class TestRegistration():

    def test_RegistrationSuccesful(self,Setup):

        rp=RegisterPage()
        rp.Getusernamefield(Setup).send_keys('testingbro')
        rp.Getemailfield(Setup).send_keys('tbro@testman.com')
        rp.Getpasswordfield(Setup).send_keys('s2sghjgksdfg')
        rp.GetRegisterbutton(Setup).click()
        mp=MainPage()
        assert mp.IsOn(Setup)

    def test_RegistrationFailedPasswordInvalid(self,Setup):

        rp = RegisterPage()
        rp.Getusernamefield(Setup).send_keys('testingbro')
        rp.Getemailfield(Setup).send_keys('tbro@testman.com')
        rp.Getpasswordfield(Setup).send_keys('1yre')
        rp.GetRegisterbutton(Setup).click()
        assert rp.ErrorDisplayed(Setup)

    """
    
    Implement the following cases when frontend team delivers design
        1. Username Invalid
            a. Repitition
            b. Format
        2. Email Invalid
            a. Repitition
            b. Format
    """




