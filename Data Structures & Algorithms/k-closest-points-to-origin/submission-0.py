import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        heap = []

        for x, y in points:
            d = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (d, x, y))
        
        for i in range(k):
            d, x, y = heapq.heappop(heap)
            result.append([x, y])
        
        return result
        