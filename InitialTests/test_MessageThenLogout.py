from GeneralUtilities import BrowserFunctions
from Pages.PMPage import PMPage
from Pages.PMComposeMessagePage import PMComposeMessagePage
from Pages.MainPage import MainPage

import unittest, pytest

@pytest.fixture()
def Setup():

    driver = BrowserFunctions.BrowserLoad()
    mp = MainPage()
    mp.Redirect(driver)
    mp.GetLoginFormButton(driver).click()
    yield driver
    driver.close()

@pytest.mark.usefixtures('Setup')
class TestMessagelogout():


    def LoggedInFirst(self,Setup):

        mp = MainPage()
        mp.Login(Setup, 'zeina3', 'Password1')
        assert mp.LoggedIn(Setup)


    def ComposeMessage(self,Setup):
            pm=PMPage(Setup).click()
            cmpm = PMComposeMessagePage()
            cmpm.GetComposeMessaging(Setup).click()
            try:
                cmpm.GetToField(Setup).send_keys('hello')
                cmpm.GetSubjectField(Setup).send_keys('hkhfkfhsd')
                cmpm.GetMessageField(Setup).send_keys('hsjkhgkhkfhkfgkghjk')
                cmpm.GetSubmitButton(Setup).click()
            except:
                assert False

            assert True

    def loggout(self,Setup):
        mp=MainPage()
        mp.GetLogOutButton().click()