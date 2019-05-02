from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage
import unittest, pytest
import random



@pytest.fixture()
def Setup():

    driver=BrowserFunctions.BrowserLoad()
    mp = MainPage()
    mp.Redirect(driver)
    mp.GetSignupFormButton(driver).click()
    yield driver
    driver.close()

@pytest.mark.usefixtures('Setup')
class TestRegistration():

    def test_RegistrationSuccesful(self,Setup):
        user=self.GenerateRandomUser()
        rp=MainPage()
        rp.Signup(Setup,user,user+"@test.com","1234567890")
        assert rp.LoggedIn(Setup)

    def test_RegistrationFailedPasswordInvalid(self,Setup):
        user = self.GenerateRandomUser()
        rp = MainPage()
        rp.Signup(Setup, user, user + "@test.com", "123")
        assert rp.SignupErrorIsOn(Setup)

    def test_RegistrationFailedRepeatedUsername(self,Setup):
        rp = MainPage()
        rp.Signup(Setup, "repateduser","new@test.com", "1234567890")
        assert rp.SignupErrorIsOn(Setup)

    def test_RegistrationFailedRepeatedEmail(self,Setup):
        rp = MainPage()
        rp.Signup(Setup, "new", "repeateduser@test.com", "1234567890")
        assert rp.SignupErrorIsOn(Setup)

    def test_RegistrationFailedWrongFormatEmail(self,Setup):
        rp = MainPage()
        rp.Signup(Setup, "new", "wrong", "1234567890")
        assert rp.SignupErrorIsOn(Setup)


    def test_Refresh(self,Setup):
        rp=MainPage()
        Setup.refresh()
        assert rp.IsOn(Setup)
        #add assert checking content is still on page



    def GenerateRandomUser(self):
        return "testuser"+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))








