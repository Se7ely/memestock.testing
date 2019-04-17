from GeneralUtilities import BrowserFunctions
from Pages.PMPage import PMPage
from Pages.ComposeMessagePage import ComposeMessagePage
from Pages.MainPage import MainPage
import unittest, pytest
from ddt import ddt, data, unpack

@pytest.fixture()
def Setup():

    driver=BrowserFunctions.BrowserLoad()
    pm= PMPage()
    pm.Redirect(driver)
    yield driver
    driver.close()


@pytest.mark.usefixtures('Setup')
class TestPM():

    def test_PMElementsDispalyed(self,Setup):
        pm=PMPage()
        try:
            pm.GetMessaging(Setup)
            pm.GetComposmessaging(Setup)
            pm.GetSent(Setup)
            pm.Getinbox(Setup)
        except:
            assert False
        assert True

    def test_ComposeMessagesElementsDisplayed(self, Setup):
        cmpm=ComposeMessagePage()
        cmpm.GetComposmessaging(Setup).click()
        try:
            cmpm.GetToText(Setup)
            cmpm.GetSubjectText(Setup)
            cmpm.GetYourMessage(Setup)
            cmpm.GetSubmitButton(Setup)
        except:
            assert False

        assert True
