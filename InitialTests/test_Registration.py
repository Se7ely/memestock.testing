from GeneralUtilities import BrowserFunctions
from Pages.RegisterPage import RegisterPage
from Pages.MainPage import MainPage
import unittest, pytest
import random
from ddt import ddt, data, unpack


@pytest.fixture()
def Setup():

    driver=BrowserFunctions.BrowserLoad()

    yield driver
    driver.close()

@pytest.mark.usefixtures('Setup')
class TestRegistration():

    def test_RegistrationSuccesful(self,Setup):
        user=self.GenerateRandomUser()
        rp=RegisterPage()
        rp.Getusernamefield(Setup).send_keys(user)
        rp.Getemailfield(Setup).send_keys(user+"@test.com")
        rp.Getpasswordfield(Setup).send_keys('1234567890')
        rp.GetRegisterbutton(Setup).click()
        mp=MainPage()
        assert mp.IsOn(Setup)

    def test_RegistrationFailedPasswordInvalid(self,Setup):
        user = self.GenerateRandomUser()
        rp = RegisterPage()
        rp.Getusernamefield(Setup).send_keys(user)
        rp.Getemailfield(Setup).send_keys(user + "@test.com")
        rp.Getpasswordfield(Setup).send_keys('1234')
        rp.GetRegisterbutton(Setup).click()
        assert rp.ErrorDisplayed(Setup)


    def test_RegistrationFailedRepeatedUsername(self,Setup):
        rp = RegisterPage()
        rp.Getusernamefield(Setup).send_keys("repeateduser")
        rp.Getemailfield(Setup).send_keys("new@test.com")
        rp.Getpasswordfield(Setup).send_keys('1234567890')
        rp.GetRegisterbutton(Setup).click()
        assert rp.ErrorDisplayed(Setup)


    def test_RegistrationFailedRepeatedEmail(self,Setup):
        rp = RegisterPage()
        rp.Getusernamefield(Setup).send_keys("new")
        rp.Getemailfield(Setup).send_keys("repeateduser@test.com")
        rp.Getpasswordfield(Setup).send_keys('1234567890')
        rp.GetRegisterbutton(Setup).click()
        assert rp.ErrorDisplayed(Setup)

    def test_RegistrationFailedWrongFormatEmail(self,Setup):
        rp = RegisterPage()
        rp.Getusernamefield(Setup).send_keys("new")
        rp.Getemailfield(Setup).send_keys("wrong")
        rp.Getpasswordfield(Setup).send_keys('1234567890')
        rp.GetRegisterbutton(Setup).click()
        mp = MainPage()
        assert not mp.IsOn(Setup)


    def test_Refresh(self,Setup):
        rp=RegisterPage()
        Setup.refresh()
        assert rp.IsOn(Setup)
        #add assert checking content is still on page



    def GenerateRandomUser(self):
        return "testuser"+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))








