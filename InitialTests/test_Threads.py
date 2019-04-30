from GeneralUtilities import BrowserFunctions
from Pages.MainPage import MainPage
from Pages.ThreadsPage import ThreadsPage

import unittest, pytest
from ddt import ddt, data, unpack


@pytest.fixture()
def Setup():

    driver=BrowserFunctions.BrowserLoad()
    tp=ThreadsPage()
    tp.Redirect(driver)

    yield driver
    driver.close()

@pytest.mark.usefixtures('Setup')
class TestThreads():


    def test_ThreadsDisplayed(self,Setup):
        tp=ThreadsPage()
        threadlist=tp.GetThreads(Setup)
        assert len(threadlist)!=0

    def test_Upvote(self,Setup):
        tp = ThreadsPage()
        threadlist = tp.GetThreads(Setup)
        for t in threadlist:
            vc=t.GetVoteCount(Setup)
            t.GetUpvoteButton(Setup).click()
            assert t.GetVoteCount(Setup)==str(vc+1)

    def test_Downvote(self,Setup):
        tp = ThreadsPage()
        threadlist = tp.GetThreads(Setup)
        for t in threadlist:
            vc = t.GetVoteCount(Setup)
            t.GetDownvoteButton(Setup).click()
            assert t.GetVoteCount(Setup) == str(vc - 1)

    def test_DoubleUpvote(self,Setup):
        tp = ThreadsPage()
        threadlist = tp.GetThreads(Setup)
        for t in threadlist:
            vc = t.GetVoteCount(Setup)
            t.GetUpvoteButton(Setup).click()
            t.GetUpvoteButton(Setup).click()
            assert t.GetVoteCount(Setup) == str(vc)

    def test_DoubleDownvote(self,Setup):
        tp = ThreadsPage()
        threadlist = tp.GetThreads(Setup)
        for t in threadlist:
            vc = t.GetVoteCount(Setup)
            t.GetDownvoteButton(Setup).click()
            t.GetDownvoteButton(Setup).click()
            assert t.GetVoteCount(Setup)==str(vc)



    def test_Refresh(self,Setup):
        tp=ThreadsPage()
        Setup.refresh()
        assert tp.IsOn(Setup)

