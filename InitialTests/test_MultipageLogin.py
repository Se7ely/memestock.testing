from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage
import unittest, pytest

@pytest.fixture()
def Setup():

    driver=BrowserFunctions.BrowserLoad()
    mp=MainPage()
    mp.Redirect(driver)

    yield driver
    driver.close()



@pytest.mark.usefixtures('Setup')
class TestMultipageLogin():

    def test_RightUsernameDisplayed(self,Setup):
        assert False
