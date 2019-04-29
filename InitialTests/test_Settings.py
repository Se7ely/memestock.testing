from GeneralUtilities import BrowserFunctions
from Pages.SettingsPage import UserSettingsPage
from Pages.ProfileSettingsPage import ProfileSettingsPage
from Pages.AccountSettingsPage import AccountSettingsPage
from Pages.MainPage import MainPage
import unittest, pytest
from ddt import ddt, data, unpack

@pytest.fixture()
def Setup():

    driver=BrowserFunctions.BrowserLoad()
    usp= UserSettingsPage()
    usp.Redirect(driver)
    yield driver
    driver.close()


@pytest.mark.usefixtures('Setup')
class TestSettings():

    def test_UserSettingElementsDispalyed(self,Setup):
        usp=UserSettingsPage()
        try:
            usp.Getprofiletab(Setup)
            usp.Getaccounttab(Setup)
        except:
            assert False
        assert True

    def test_ProfileSettingsElementsDisplayed(self, Setup):
        psp=ProfileSettingsPage()
        psp.Getprofiletab(Setup).click()
        try:
            psp.Getdisplaynamefield(Setup)
            psp.Getbiofield(Setup)
        except:
            assert False

        assert True

    def test_AccountSettingsElementsdisplayed(self,Setup):
        asp=AccountSettingsPage()
        asp.Getaccounttab(Setup).click()
        try:
            asp.Getchangeorupdateemail(Setup)
            asp.Getchangepassword(Setup)

        except:
            assert  False

        assert True

    def test_UpdateEmailTextDisplayed(self, Setup):
        asp = AccountSettingsPage()
        asp.Getaccounttab(Setup).click()
        asp.Getchangeorupdateemail(Setup).click()
        try:
            asp.Getpupdatemailbutton(Setup)
            asp.GetupdateEmail(Setup)
        except:
            assert False

        assert True

    def test_ChangePasswordElementsDisplayed(self, Setup):
        asp = AccountSettingsPage()
        asp.Getaccounttab(Setup).click()
        asp.Getchangepassword(Setup).click()
        try:
            asp.Getnewpassword(Setup)
            asp.Getoldpassword(Setup)
            asp.Getsubbutton(Setup)
        except:
            assert False

        assert True

    def test_Refresh(self,Setup):
        usp=UserSettingsPage()
        Setup.refresh()
        assert usp.IsOn(Setup)
        #add assert checking content is still on page

