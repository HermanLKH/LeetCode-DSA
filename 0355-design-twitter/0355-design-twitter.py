class User:
    __slots__ = ("tweets", "followees")

    def __init__(self):
        self.tweets = []
        self.followees = set()

class Twitter:
    def __init__(self):
        self.users = {}
        self.time = 0

    def _createUser(self, userId):
        if userId not in self.users:
            self.users[userId] = User()

    # Time complexity: O(1)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self._createUser(userId)
        tweets = self.users[userId].tweets
        tweets.append((self.time, tweetId))
        self.time -= 1
        
        # Time complexity: O(1) => O(10)
        # at most 10 elements
        if len(tweets) > 10:
            tweets.pop(0)

    # Time complexity: O(F + 1) => O(F + 1) + O(log (F + 1))
    # F => number of followees
    # 10 most recent tweetIds of userId/ followers
    def getNewsFeed(self, userId: int) -> list[int]:
        # Time complexity: O(1)
        if userId not in self.users:
            return []

        # Time complexity: O(1)
        followees = self.users[userId].followees
        latestTweets = []
        latestFeeds = []

        # Time complexity: O(F + 1)
        for uid in chain(followees, (userId, )):
            if not self.users[uid].tweets:
                continue

            tweets = self.users[uid].tweets
            index = len(tweets) - 1
            time, tweetId = tweets[index]
            latestTweets.append((time, tweetId, uid, index))

        # Time complexity: O(F + 1)
        heapq.heapify(latestTweets)

        # Time complexity: O(log (F + 1)) => 10 x 2 x log (F + 1)
        while len(latestFeeds) < 10 and latestTweets:
            # Time complexity: O(log F + 1)
            time, tweetId, uid, index = heapq.heappop(latestTweets)
            latestFeeds.append(tweetId)

            if index > 0:
                time, tweetId = self.users[uid].tweets[index - 1]
                # Time complexity: O(log F + 1)
                heapq.heappush(latestTweets, (time, tweetId, uid, index - 1))

        return latestFeeds
    
    # Time complexity: O(1)
    # followerId follows followeeId
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        
        self._createUser(followerId)
        self._createUser(followeeId)
        self.users[followerId].followees.add(followeeId)

    # Time complexity: O(1)
    # followerId unfollows followeeId
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self._createUser(followerId)
        self._createUser(followeeId)
        self.users[followerId].followees.discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)