class Twitter:

    def __init__(self):
        self.users = {}
        self.count = 0

    # unique tweetId, userId
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1

        if userId not in self.users:
            self.users[userId] = ([], set())  # tweetIds, followeeIds

        self.users[userId][0].append((self.count, tweetId))  ## append latest tweetId to stack

    # 10 most recent tweetIds of userId/ followers
    def getNewsFeed(self, userId: int) -> list[int]:
        if userId not in self.users:
            return []

        followees = self.users[userId][1]
        latestTweets = []
        latestFeeds = []

        for uid in followees | {userId}:
            if not self.users[uid][0]:
                continue

            tweets = self.users[uid][0]
            index = len(tweets) - 1
            time, tweetId = tweets[index]
            latestTweets.append((time, tweetId, uid, index))

        heapq.heapify(latestTweets)

        while len(latestFeeds) < 10 and latestTweets:
            time, tweetId, uid, index = heapq.heappop(latestTweets)
            latestFeeds.append(tweetId)

            if index > 0:
                time, tweetId = self.users[uid][0][index - 1]
                heapq.heappush(latestTweets, (time, tweetId, uid, index - 1))

        return latestFeeds
        
    # followerId follows followeeId
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        if followerId not in self.users:
            self.users[followerId] = ([], set())

        if followeeId not in self.users:
            self.users[followeeId] = ([], set())

        self.users[followerId][1].add(followeeId)

    # followerId unfollows followeeId
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            return

        self.users[followerId][1].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)