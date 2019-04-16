from GeneralUtilities import BrowserFunctions
from Pages.MyProfilePage import MyProfilePage
from Pages.MainPage import MainPage
import unittest, pytest
from ddt import ddt, data, unpack

@pytest.fixture()
def Setup():

    driver=BrowserFunctions.BrowserLoad()
    mpf= MyProfilePage()
    mpf.Redirect(driver)
    yield driver
    driver.close()


@pytest.mark.usefixtures('Setup')
class TestMyProfile():

    def test_MyProfileElementsDisplayed(self,Setup):
        mpf=MyProfilePage()
        try:
            mpf.GetOverViewedButton(Setup)
            mpf.GetPostsButton(Setup)
            mpf.GetCommentsButton(Setup)
            mpf.GetSavedButton(Setup)
            mpf.GetHiddenButton(Setup)
            mpf.GetProfilename(Setup)

        except:
            assert False
        assert True
