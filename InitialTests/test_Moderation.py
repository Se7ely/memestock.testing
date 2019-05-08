from GeneralUtilities import BrowserFunctions
from Pages.ModerationPage import ModerationPage
from Pages.BanUserModerationPage import BanUserModerationPage
from Pages.InviteModeratorsModerationPage import InviteModeratorsModerationPage


from Pages.MainPage import MainPage
import unittest, pytest


@pytest.fixture()
def Setup():

    driver=BrowserFunctions.BrowserLoad()
    mdp= ModerationPage()
    mdp.Redirect(driver)
    yield driver
    driver.close()


@pytest.mark.usefixtures('Setup')
class TestModeration():

    def test_ModerationElementsDisplayed(self,Setup):
        mdp=ModerationPage()
        try:
            mdp.GetModerator(Setup)
            mdp.GetModerationQueue(Setup)
            mdp.GetBanUsers(Setup)
        except:
            assert False
        assert True

    def test_InviteModeratorsElementsDisplayed(self, Setup):
        imdp=InviteModeratorsModerationPage()
        imdp.GetModerator(Setup).click()
        try:
            imdp.GetSelect(Setup)
            imdp.GetGetUser(Setup)
            imdp.GetInviteButton(Setup)
        except:
            assert False

        assert True

    def test_BanUserModerationElementsdisplayed(self,Setup):
        bumdp=BanUserModerationPage()
        bumdp.GetBanUsers(Setup).click()

        try:

            bumdp.GetSelectUserBan(Setup)
            bumdp.GetGetUserBanself(Setup)
            bumdp.GetDoneButton(Setup)
            bumdp.GetBanUserCheckBox(Setup)
            bumdp.GetUnBanUserCheckBox(Setup)

        except:
            assert  False

        assert True

    def test_Refresh(self,Setup):
        mdp=ModerationPage()
        Setup.refresh()
        assert mdp.IsOn(Setup)
        #add assert checking content is still on page


