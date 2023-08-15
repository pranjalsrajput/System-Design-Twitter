"""
Requirements:

TwitterClass()
post_tweet()
follow
unfollow
get_news_feed -> 10 recent tweets of followees
"""
import heapq
from collections import defaultdict


class Twitter:
    def __init__(self):
        self.count = 0
        self.follow_map = defaultdict(set)  # Store a user as a key and set of it's followees as values in a map
        self.tweet_map = defaultdict(
            list)  # Store a user as key and store list of its tweets, each as a list of [count, tweet_id],
        # where count is the tweet number of the user, as values in a map. We are maintaining the negative
        # count, as we will be using minheap for retrieving the 10 latest tweets.

    def post_tweet(self, user_id: int, tweet_id: int):
        self.tweet_map[user_id].append([self.count, tweet_id])
        self.count -= 1

    def follow(self, follower_id: int, followee_id: int):
        # O(1) complexity
        self.follow_map[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int):
        # O(1) complexity
        if followee_id in self.follow_map[follower_id]:
            self.follow_map[follower_id].remove(followee_id)

    def get_news_feed(self, user_id: int) -> []:
        """
        We use minheap to find the latest 10 tweets of the followees of the given follower/user.
        We first retrieve the latest tweets of all the followees of the follower. Then we compare the timestamp (
        which is represented by count here) of these tweets and select the one with the minimum value. We then
        decrease the index of this followees tweet list to get its previous tweet, and then compare this tweet's
        timestamp with the timstamp of the other two tweets and then selects the one with the minimum value. This
        process is repeated until we have maximum of 10 tweets.
        :param user_id:
        :return:
        """
        min_heap = []
        result = []
        self.follow_map[user_id].add(user_id)

        for followee_id in self.follow_map[user_id]:
            if followee_id in self.tweet_map:
                index = len(self.tweet_map[followee_id]) - 1  # Get index of the last tweet
                count, tweet_id = self.tweet_map[followee_id][index]
                min_heap.append(
                    [count, tweet_id, followee_id, index - 1])  # index is reduced by 1 to go to the previous element

        heapq.heapify(min_heap)
        while min_heap and len(result) < 10:
            count, tweet_id, followee_id, index = heapq.heappop(min_heap)
            result.append(tweet_id)
            if index >= 0:
                count, tweet_id = self.tweet_map[followee_id][index]
                heapq.heappush(min_heap, [count, tweet_id, followee_id, index - 1])
        return result


twitter = Twitter()

twitter.follow(1, 2)
twitter.follow(1, 3)
twitter.follow(1, 4)

twitter.post_tweet(1, 1)
twitter.post_tweet(1, 2)
twitter.post_tweet(1, 3)
twitter.post_tweet(3, 31)
twitter.post_tweet(2, 21)
twitter.post_tweet(2, 22)
twitter.post_tweet(2, 23)
twitter.post_tweet(2, 24)
twitter.post_tweet(2, 25)
twitter.post_tweet(2, 26)
twitter.post_tweet(2, 27)
twitter.post_tweet(2, 28)
twitter.post_tweet(2, 29)

twitter.post_tweet(3, 32)
twitter.post_tweet(2, 231)
twitter.post_tweet(3, 33)

print(twitter.get_news_feed(1))
