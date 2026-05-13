class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        l = 0
        for r in range(len(nums)):
            if (r - l + 1) == k:
                result.append(max(nums[l:r + 1]))
                l += 1
        
        return result

        