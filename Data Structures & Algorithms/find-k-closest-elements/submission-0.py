class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for num in arr:
            heapq.heappush(heap, (abs(num - x), num))
        
        res = []
        for _ in range(k):
            dist, val = heapq.heappop(heap)
            res.append(val)
        
        return sorted(res)