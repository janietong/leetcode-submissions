"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap = []
        intervals.sort(key=lambda i: i.start)
        res = 0
        for interval in intervals:
            start, end = interval.start, interval.end
            if not heap or start < heap[0]:
                res += 1
            else:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        return res
        