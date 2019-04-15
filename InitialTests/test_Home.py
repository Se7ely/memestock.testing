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

    def test_ThreadsDisplayed(self,Setup):
        mp=MainPage()
        threadlist=mp.GetThreads(Setup)
        assert len(threadlist)!=0

    def test_Upvote(self,Setup):
        mp = MainPage()
        threadlist = mp.GetThreads(Setup)
        for t in threadlist:
            t.GetUpvoteButton(Setup).click()
            assert t.GetVoteCount(Setup)=='1'

    def test_Downvote(self,Setup):
        mp = MainPage()
        threadlist = mp.GetThreads(Setup)
        for t in threadlist:
            t.GetDownvoteButton(Setup).click()
            assert t.GetVoteCount(Setup)=='-1'

    def test_DoubleUpvote(self,Setup):
        mp = MainPage()
        threadlist = mp.GetThreads(Setup)
        for t in threadlist:
            t.GetUpvoteButton(Setup).click()
            t.GetUpvoteButton(Setup).click()
            assert t.GetVoteCount(Setup)=='0'

    def test_DoubleDownvote(self,Setup):
        mp = MainPage()
        threadlist = mp.GetThreads(Setup)
        for t in threadlist:
            t.GetDownvoteButton(Setup).click()
            t.GetDownvoteButton(Setup).click()
            assert t.GetVoteCount(Setup)=='0'





