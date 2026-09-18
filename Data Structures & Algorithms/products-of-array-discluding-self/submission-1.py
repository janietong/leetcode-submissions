class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftToRight = [1] * n
        rightToLeft = [1] * n

        for i in range(1, n):
            leftToRight[i] = nums[i - 1] * leftToRight[i - 1]
        for i in range(n - 2, -1, -1):
            rightToLeft[i] = nums[i + 1] * rightToLeft[i + 1]
        
        res = [1] * n
        for i in range(n):
            res[i] = leftToRight[i] * rightToLeft[i]
        
        return res