class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = float('inf')

        while l <= r:
            m = (l + r) // 2
            count = 0
            for amount in piles:
                count += math.ceil(amount / m)

            if count <= h:
                result = m
                r = m - 1
            else:
                l = m + 1
        
        return result