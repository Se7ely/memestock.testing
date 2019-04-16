from GeneralUtilities import BrowserFunctions
from Pages.CreatePostPage import CreatePostPage
import unittest, pytest
from ddt import ddt, data, unpack


@pytest.fixture()
def Setup():

    driver=BrowserFunctions.BrowserLoad()
    cpp=CreatePostPage()
    cpp.Redirect(driver)

    yield driver
    driver.close()

@pytest.mark.usefixtures('Setup')
class TestCreatePost():

    def test_AllVitalElementsDisplayed(self, Setup):
        cpp = CreatePostPage()
        try:
            cpp.Getsubredditfield(Setup)
            cpp.Gettitlefield(Setup)
            cpp.Getbodyfield(Setup)
            cpp.Getcreatebutton(Setup)
        except:
            assert False

        assert True

    def test_CreatePost(self,Setup):
        cpp=CreatePostPage()
        cpp.Getsubredditfield(Setup).send_keys('sfghjkjyjurytryhtjfgkh')
        cpp.Gettitlefield(Setup).send_keys('YTTHJFTYHJUYGH')
        cpp.Getbodyfield(Setup).send_keys('dadewfwegrhhsgsehshrsh, rgerhrgwrgewwegwegwege')
        cpp.Getcreatebutton(Setup).click()
        #add assert onpage when their is response
        #add assert post is created as input
        assert False

    def test_Refresh(self,Setup):
        cpp=CreatePostPage()
        Setup.refresh()
        assert cpp.IsOn(Setup)
        #add assert checking content is still on page
