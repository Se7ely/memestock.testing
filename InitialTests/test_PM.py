from GeneralUtilities import BrowserFunctions
from Pages.PMPage import PMPage
from Pages.PMComposeMessagePage import PMComposeMessagePage
from Pages.MainPage import MainPage
import unittest, pytest

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
            pm.GetComposeMessaging(Setup)
            pm.GetSent(Setup)
            pm.GetInbox(Setup)
        except:
            assert False
        assert True

    def test_ComposeMessagesElementsDisplayed(self, Setup):
        cmpm=PMComposeMessagePage()
        cmpm.GetComposeMessaging(Setup).click()
        try:
            cmpm.GetToField(Setup)
            cmpm.GetSubjectField(Setup)
            cmpm.GetMessageField(Setup)
            cmpm.GetSubmitButton(Setup)
        except:
            assert False

        assert True

    def test_Refresh(self,Setup):
        pm=PMPage()
        Setup.refresh()
        assert pm.IsOn(Setup)
        #add assert checking content is still on page