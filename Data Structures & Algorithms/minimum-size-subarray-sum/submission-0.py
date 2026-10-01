class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float('inf')
        l = 0
        curCount = 0
        for r in range(len(nums)):
            curCount += nums[r]
            while curCount >= target:
                minLen = min(r - l + 1, minLen)
                curCount -= nums[l]
                l += 1
        return minLen if minLen != float('inf') else 0