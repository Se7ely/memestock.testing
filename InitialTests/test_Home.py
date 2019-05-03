from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage
from Pages.CreateCommunityPage import CreateCommunityPage
import unittest, pytest



@pytest.fixture()
def Setup():

    driver=BrowserFunctions.BrowserLoad()
    mp=MainPage()
    mp.Redirect(driver)

    yield driver
    driver.close()

@pytest.mark.usefixtures('Setup')
class TestHome():

    def test_AllVitalElementsDisplayed(self, Setup):
        mp=MainPage()
        try:
            mp.GetCreatePostButton(Setup)
            mp.GetLogoButton(Setup)
            mp.GetNotificationsButton(Setup)
            mp.GetPmButton(Setup)
            mp.GetSearchBar(Setup)
            mp.GetTotoPanchor(Setup)
        except:
            assert False

        assert True



    def test_Refresh(self,Setup):
        mp=MainPage()
        Setup.refresh()
        assert mp.IsOn(Setup)
        #add assert checking content is still on page



    def test_CommunityPageDisplayed(self, Setup):
        cmd = CreateCommunityPage()
        cmd.GetCommunityButton().click()

        try:
            cmd.GetSubRedditBio(Setup)
            cmd.GetSubRedditCoverPhoto(Setup)
            cmd.GetSubRedditModerator(Setup)
            cmd.GetSubRedditNameField(Setup)
            cmd.GetSubRedditRuleFields(Setup)
            cmd.GetSubRedditCreateButton(Setup)

        except:
            assert False

        assert True