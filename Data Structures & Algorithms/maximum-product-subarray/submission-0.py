class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin = 1
        curMax = 1

        for n in nums:
            if n == 0:
                curMin = 1
                curMax = 1
            cand = (n, curMin * n, curMax * n)
            curMax = max(cand)
            curMin = min(cand)
            res = max(curMax, res)
        return res
        