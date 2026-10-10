class User:
    def __init__(self, userId):
        self.userId = userId
        self.tweets = []
        self.followees = set()

class Twitter:

    def __init__(self):
        self.users = {}
        self.time = 0

    def _createUser(self, userId):
        if userId not in self.users:
            self.users[userId] = User(userId)

    # unique tweetId, userId
    def postTweet(self, userId: int, tweetId: int) -> None:
        self._createUser(userId)
        self.users[userId].tweets.append((self.time, tweetId))
        self.time -= 1

    # 10 most recent tweetIds of userId/ followers
    def getNewsFeed(self, userId: int) -> list[int]:
        if userId not in self.users:
            return []

        followees = self.users[userId].followees
        latestTweets = []
        latestFeeds = []

        for uid in followees | {userId}:
            if not self.users[uid].tweets:
                continue

            tweets = self.users[uid].tweets
            index = len(tweets) - 1
            time, tweetId = tweets[index]
            latestTweets.append((time, tweetId, uid, index))

        heapq.heapify(latestTweets)

        while len(latestFeeds) < 10 and latestTweets:
            time, tweetId, uid, index = heapq.heappop(latestTweets)
            latestFeeds.append(tweetId)

            if index > 0:
                time, tweetId = self.users[uid].tweets[index - 1]
                heapq.heappush(latestTweets, (time, tweetId, uid, index - 1))

        return latestFeeds
        
    # followerId follows followeeId
    def follow(self, followerId: int, followeeId: int) -> None:
        self._createUser(followerId)
        self._createUser(followeeId)
        self.users[followerId].followees.add(followeeId)

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