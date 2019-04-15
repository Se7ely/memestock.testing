from GeneralUtilities import BrowserFunctions
from Pages.UserSettingsPage import UserSettingsPage
from Pages.ProfileSettingsPage import ProfileSettingsPage
from Pages.AccountSettingsPage import AccountSettingsPage
from Pages.MainPage import MainPage
import unittest, pytest
import pytest_html

from ddt import ddt, data, unpack

@pytest.fixture()
def Setup():

    driver=BrowserFunctions.BrowserLoad()
    us= UserSettingsPage()
    us.Redirect(driver)
    yield driver
    driver.close()


@pytest.mark.usefixtures('Setup')
class TestSettings():

    def test_UserSettingElementsDispalyed(self,Setup):
        usp=UserSettingsPage()
        usp.Redirect(Setup)
        try:
            usp.Getprofiletab(Setup)
            usp.Getaccounttab(Setup)
        except:
            assert False
        assert True
"""""
    def test_ProfileSettingsElementsDisplayed(self, Setup):
        ps=ProfileSettingsPage()
        ps.Redirect(Setup)
        try:
            ps.Getdisplaynamefield(Setup)
            ps.Getbiofield(Setup)
        except:
            assert False

        assert True

    def test_AccountSettingsElementsdisplayed(self,Setup):
         acc=AccountSettingsPage()
         acc.Redirect(Setup)
         try:
             acc.Getchangeorupdateemail(Setup)
             acc.Getchangepassword(Setup)

         except:
             assert  False

         assert True

    def test_UpdateEmailTextDisplayed(self, Setup):
        acc = AccountSettingsPage()
        acc.Getchangeorupdateemail(Setup).click()
        try:
            acc.Getpupdatemailbutton(Setup)
            acc.GetupdateEmail(Setup)
        except:
            assert False

        assert True

    def test_ChangePasswordElementsDisplayed(self, Setup):
        acc = AccountSettingsPage()
        acc.Getchangepassword(Setup).click()
        try:
            acc.Getnewpassword(Setup)
            acc.Getoldpassword(Setup)
            acc.Getsubbutton(Setup)
        except:
            assert False

        assert True
"""