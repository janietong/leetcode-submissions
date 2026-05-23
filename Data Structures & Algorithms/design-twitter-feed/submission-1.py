from collections import defaultdict
class Twitter:

    def __init__(self):
        self.time = 0
        self.heap = []
        self.follows = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        heapq.heappush(self.heap, (-self.time, userId, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        temp = []
        count = 0
        while count < 10 and self.heap:
            t, user, tweet = heapq.heappop(self.heap)
            if user == userId or user in self.follows[userId]:
                result.append(tweet)
                count += 1
            temp.append((t, user, tweet))
        
        for t, user, tweet in temp:
            heapq.heappush(self.heap, (t, user, tweet))
        return result

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        
