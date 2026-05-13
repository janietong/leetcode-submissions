class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        for key, val in d.items():
            heapq.heappush(heap, (-val, key))
        
        result = []
        for i in range(k):
            v, k = heapq.heappop(heap)
            result.append(k)
        
        return result
            
        