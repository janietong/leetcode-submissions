class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        res = 0
        curSum = 0

        for num in nums:
            curSum += num
            res += seen.get(curSum - k, 0)
            seen[curSum] = seen.get(curSum, 0) + 1
        
        return res