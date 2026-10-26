class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxEnd = 0

        for i, num in enumerate(nums):
            if i > maxEnd:
                return False
            
            maxEnd = max(maxEnd, i + num)
        return True