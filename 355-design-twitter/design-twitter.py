import heapq
from collections import defaultdict
from typing import List

class Twitter:
    def __init__(self):
        # Dictionary to keep track of followers for each user.
        # Key: UserId, Value: Set of UserIds that this user follows.
        self.followers = defaultdict(set)
        
        # Dictionary to keep track of tweets for each user.
        # Key: UserId, Value: List of tuples, each containing a timestamp (count) and a tweetId.
        self.tweets = defaultdict(list)
        
        # Global counter to simulate the passage of time for tweets.
        # This helps maintain the order of tweets, with lower numbers indicating more recent tweets.
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # When a user posts a tweet, it is recorded with the current timestamp (count).
        # The tweet is appended to the list of tweets for that user.
        self.tweets[userId].append((self.count, tweetId))
        
        # Decrement the count to ensure that more recent tweets have a lower count value,
        # which allows them to appear first when using a max-heap.
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # List to store the final news feed result (up to 10 most recent tweets).
        result = []
        
        # Max-heap to help retrieve the most recent tweets from followed users.
        maxheap = []

        # A user should see their own tweets in their news feed, so we add the user to their own follower list.
        self.followers[userId].add(userId)

        # Collect the most recent tweet from each followed user and add it to the heap.
        for follower_userid in self.followers[userId]:
            if follower_userid in self.tweets:
                # Get the index of the most recent tweet for this user.
                index = len(self.tweets[follower_userid]) - 1
                
                # Extract the count (timestamp) and tweetId of the most recent tweet.
                cnt, tweetid = self.tweets[follower_userid][index]
                
                # Add the tweet to the max-heap. The heap is structured by the count, with the most recent tweets
                # (lowest count values) being prioritized.
                maxheap.append((cnt, tweetid, follower_userid, index))
            
        # Convert the list to a heap structure.
        heapq.heapify(maxheap)

        # Extract the top 10 most recent tweets by continuously popping from the heap.
        while maxheap and len(result) < 10:
            # Pop the most recent tweet from the heap.
            cnt, tweetid, follower_userid, index = heapq.heappop(maxheap)
            
            # Add the tweetId to the result list.
            result.append(tweetid)
            
            # Move to the next most recent tweet from the same user (if any).
            index -= 1
            if index >= 0:
                # If there are more tweets from this user, add the next one to the heap.
                cnt, tweetid = self.tweets[follower_userid][index]
                heapq.heappush(maxheap, (cnt, tweetid, follower_userid, index))
        
        # Return the list of tweetIds in the order they should appear in the news feed.
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        # Add the followee to the set of users that the followerId is following.
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove the followee from the followerId's set of followed users,
        # but only if the followerId is currently following the followeeId.
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
