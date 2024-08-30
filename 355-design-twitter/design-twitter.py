class Twitter:
    def __init__(self):

        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count,tweetId))
        self.count -= 1


    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        maxheap = []

        self.followers[userId].add(userId)

        for follower_userid in self.followers[userId]:
            if follower_userid in self.tweets:
                index = len(self.tweets[follower_userid]) - 1
                cnt , tweetid = self.tweets[follower_userid][index]
                maxheap.append((cnt,tweetid,follower_userid,index))
            
        heapq.heapify(maxheap)

        while maxheap and len(result) < 10:
            cnt,tweetid,follower_userid,index = heapq.heappop(maxheap)
            result.append(tweetid)
            index -= 1
            if index >= 0:
                cnt , tweetid = self.tweets[follower_userid][index]
                heapq.heappush(maxheap,(cnt,tweetid,follower_userid,index))
        
        return result



        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)