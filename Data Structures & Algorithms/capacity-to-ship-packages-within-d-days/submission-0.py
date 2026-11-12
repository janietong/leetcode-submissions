class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        def helperDays(maxWeight):
            res = 0
            count = 0
            for num in weights:
                if count + num > maxWeight:
                    count = num
                    res += 1
                else:
                    count += num
            
            return res

        while l <= r:
            m = (l + r) // 2 
            if helperDays(m) < days:
                r = m - 1
            else:
                l = m + 1
        
        return l
