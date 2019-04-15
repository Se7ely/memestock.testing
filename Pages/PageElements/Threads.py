

class Thread():

    def __init__(self,index):
        self.xpath='//div[@class="listingsContainer"]/div['+str(index)+']'
        self.subreddit=self.xpath+'//a[@class="threadSubreddit"]'
        self.username=self.xpath+'//div[@class="threadUsername"]'
        self.title = self.xpath + '//div[@class="threadTitle"]'
        self.content = self.xpath + '//p[@class="threadContent"]'
        self.comments = self.xpath + '//p[@class="threadComments"]'
        self.upvote=self.xpath+'//span[@class="incrementVotes"]'
        self.downvote = self.xpath + '//span[@class="decrementVotes"]'
        self.votecount=self.xpath+'//div[@class="threadUpvotes"]'

    def GetUpvoteButton(self,driver):
        return driver.find_element_by_xpath(self.upvote)

    def GetDownvoteButton(self,driver):
        return driver.find_element_by_xpath(self.downvote)

    def GetVoteCount(self,driver):
        return driver.find_element_by_xpath(self.votecount).text



