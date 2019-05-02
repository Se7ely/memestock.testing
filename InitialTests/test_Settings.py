from GeneralUtilities import BrowserFunctions
from Pages.SettingsPage import SettingsPage
from Pages.ProfileSettingsPage import ProfileSettingsPage
from Pages.AccountSettingsPage import AccountSettingsPage
from Pages.AccountSettingsPageEmail import AccountSettingsPageEmail
from Pages.AccountSettingsPagePassword import AccountSettingsPagePassword

from Pages.MainPage import MainPage
import unittest, pytest


@pytest.fixture()
def Setup():

    driver=BrowserFunctions.BrowserLoad()
    usp= SettingsPage()
    usp.Redirect(driver)
    yield driver
    driver.close()


@pytest.mark.usefixtures('Setup')
class TestSettings():

    def test_UserSettingElementsDispalyed(self,Setup):
        usp=SettingsPage()
        try:
            usp.GetProfileTab(Setup)
            usp.GetAccountTab(Setup)
        except:
            assert False
        assert True

    def test_ProfileSettingsElementsDisplayed(self, Setup):
        psp=ProfileSettingsPage()
        psp.GetProfileTab(Setup).click()
        try:
            psp.Getdisplaynamefield(Setup)
            psp.Getbiofield(Setup)
        except:
            assert False

        assert True

    def test_AccountSettingsElementsdisplayed(self,Setup):
        asp=AccountSettingsPage()
        asp.GetAccountTab(Setup).click()
        try:
            asp.GetChangeOrUpdateEmail(Setup)
            asp.GetChangePassword(Setup)

        except:
            assert  False

        assert True

    def test_UpdateEmailTextDisplayed(self, Setup):
        asp = AccountSettingsPage()
        asp.GetAccountTab(Setup).click()
        asp.GetChangeOrUpdateEmail(Setup).click()
        aspe=AccountSettingsPageEmail()
        try:
            aspe.GetUpdateEmailButton(Setup)
            aspe.GetUpdateEmail(Setup)
        except:
            assert False

        assert True

    def test_ChangePasswordElementsDisplayed(self, Setup):
        asp = AccountSettingsPage()
        asp.GetAccountTab(Setup).click()
        asp.GetChangePassword(Setup).click()
        aspp=AccountSettingsPagePassword()
        try:
            aspp.GetNewPassword(Setup)
            aspp.GetOldPassword(Setup)
            aspp.GetSubButton(Setup)
        except:
            assert False

        assert True

    def test_Refresh(self,Setup):
        usp=SettingsPage()
        Setup.refresh()
        assert usp.IsOn(Setup)
        #add assert checking content is still on page

