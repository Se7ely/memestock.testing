from GeneralUtilities import BrowserFunctions
from Pages.SettingsPage import SettingsPage
from Pages.ProfileSettingsPage import ProfileSettingsPage
from Pages.AccountSettingsPage import AccountSettingsPage
from Pages.AccountSettingsPageEmail import AccountSettingsPageEmail
from Pages.AccountSettingsPagePassword import AccountSettingsPagePassword

from Pages.MainPage import MainPage
import unittest, pytest
from ddt import ddt, data, unpack

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
        aspe=AccountSettingsPageEmail()
        try:
            aspe.Getpupdatemailbutton(Setup)
            aspe.GetupdateEmail(Setup)
        except:
            assert False

        assert True

    def test_ChangePasswordElementsDisplayed(self, Setup):
        asp = AccountSettingsPage()
        asp.Getaccounttab(Setup).click()
        asp.Getchangepassword(Setup).click()
        aspp=AccountSettingsPagePassword()
        try:
            aspp.Getnewpassword(Setup)
            aspp.Getoldpassword(Setup)
            aspp.Getsubbutton(Setup)
        except:
            assert False

        assert True

    def test_Refresh(self,Setup):
        usp=SettingsPage()
        Setup.refresh()
        assert usp.IsOn(Setup)
        #add assert checking content is still on page

