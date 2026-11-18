class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        minSoFar = maxSoFar = 1

        for num in nums:
            if num == 0:
                minSoFar = 1
                maxSoFar = 1
                continue
            tmp = maxSoFar * num
            maxSoFar = max(num, tmp, minSoFar * num)
            minSoFar = min(num, tmp, minSoFar * num)
            res = max(maxSoFar, res)
        return res