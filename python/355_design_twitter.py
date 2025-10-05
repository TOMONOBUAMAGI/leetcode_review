import heapq
from typing import List


class Twitter:
    """
    A simplified Twitter implementation that supports posting tweets,
    following/unfollowing users, and retrieving the most recent news feed.
    """

    def __init__(self):
        """
        Initialize the Twitter object.
        """
        self.user_tweets = {}
        self.user_follows = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet by a user.

        Args:
            userId (int): ID of the user posting the tweet.
            tweetId (int): ID of the tweet.
        """
        tweet = [self.timestamp, tweetId]
        if userId in self.user_tweets:
            self.user_tweets[userId].append(tweet)
        else:
            self.user_tweets[userId] = [tweet]

        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet IDs in the user's news feed.
        The news feed consists of tweets posted by the user themselves
        and the users they follow.

        Args:
            userId (int): ID of the user.

        Returns:
            List[int]: List of up to 10 most recent tweet IDs.
        """
        following_user_ids = [userId]
        if userId in self.user_follows:
            following_user_ids += self.user_follows[userId]

        following_user_tweets = []
        for following_user_id in following_user_ids:
            if following_user_id in self.user_tweets:
                following_user_tweets += self.user_tweets[following_user_id]

        heap = []
        for tweet in following_user_tweets:
            if len(heap) < 10:
                heapq.heappush(heap, tweet)
            elif tweet[0] > heap[0][0]:
                heapq.heappop(heap)  # remove the oldest tweet
                heapq.heappush(heap, tweet)

        return_tweets = []
        while heap:
            return_tweets.append(heapq.heappop(heap)[1])

        return_tweets.reverse()
        return return_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follow another user.

        Args:
            followerId (int): ID of the follower.
            followeeId (int): ID of the followee.
        """
        if followerId in self.user_follows and followeeId not in self.user_follows[followerId]:
            self.user_follows[followerId].append(followeeId)
        else:
            self.user_follows[followerId] = [followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Unfollow a user.

        Args:
            followerId (int): ID of the follower.
            followeeId (int): ID of the followee.
        """
        if followerId in self.user_follows:
            self.user_follows[followerId].remove(followeeId)
