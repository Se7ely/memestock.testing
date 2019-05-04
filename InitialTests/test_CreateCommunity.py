from GeneralUtilities import BrowserFunctions
from Pages.CreateCommunityPage import CreateCommunityPage
import unittest, pytest



@pytest.fixture()
def Setup():

    driver=BrowserFunctions.BrowserLoad()
    cmd=CreateCommunityPage()
    cmd.Redirect(driver)

    yield driver
    driver.close()

@pytest.mark.usefixtures('Setup')
class TestCreatePost():

    def test_AllVitalElementsDisplayed(self, Setup):
        cmd = CreateCommunityPage()


        try:
            cmd.GetSubRedditBio(Setup)
            cmd.GetSubRedditCoverPhoto(Setup)
            cmd.GetSubRedditModerator(Setup)
            cmd.GetSubRedditNameField(Setup)
            cmd.GetSubRedditRuleFields(Setup)
            cmd.GetSubRedditCreateButton(Setup)
        except:
            assert False

        assert True

    def test_CreatePost(self,Setup):
        cmd=CreateCommunityPage()
        cmd.GetSubRedditCoverPhoto(Setup)
        cmd.GetSubRedditModerator(Setup).send_keys('mohamed,james')
        cmd.GetSubRedditNameField(Setup).send_keys('jamesbond')
        cmd.GetSubRedditRuleFields(Setup).send_keys('hkgkggkg,hkjhkjhkhkj,khkjhkhk')
        cmd.GetSubRedditCreateButton(Setup).click()
        #add assert onpage when their is response
        #add assert post is created as input
        assert False

    def test_Refresh(self,Setup):
        cmd=CreateCommunityPage()
        Setup.refresh()
        assert cmd.IsOn(Setup)
        #add assert checking content is still on page
