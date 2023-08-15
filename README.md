# System-Design-Twitter
System design of twitter with some basic functionalities

### Requirements:

- TwitterClass()
- post_tweet()
- follow
- unfollow
- get_news_feed -> 10 recent tweets of followees

Explanation of get_news_feed method:

We use minheap to find the latest 10 tweets of the followees of the given follower/user.
We first retrieve the latest tweets of all the followees of the follower. Then we compare the timestamp (
which is represented by count here) of these tweets and select the one with the minimum value. We then
decrease the index of this followees tweet list to get its previous tweet, and then compare this tweet's
timestamp with the timstamp of the other two tweets and then selects the one with the minimum value. This
process is repeated until we have maximum of 10 tweets.