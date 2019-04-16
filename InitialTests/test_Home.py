from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage
import unittest, pytest
from ddt import ddt, data, unpack


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
            mp.Getcreatepostbutton(Setup)
            mp.Getlogobutton(Setup)
            mp.Getnotificationsbutton(Setup)
            mp.Getpmbutton(Setup)
            mp.Getsearchbar(Setup)
            mp.Gettotopanchor(Setup)
            mp.Getyourstuffdrop(Setup)
        except:
            assert False

        assert True





