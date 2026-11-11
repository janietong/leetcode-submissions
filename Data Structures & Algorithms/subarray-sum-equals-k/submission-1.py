class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        curSum = 0
        res = 0

        for num in nums:
            curSum += num
            res += d.get(curSum - k, 0)
            d[curSum] = d.get(curSum, 0) + 1
        
        return res