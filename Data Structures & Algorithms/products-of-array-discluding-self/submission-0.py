class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        pre = [0] * len(nums)
        post = [0] * len(nums)

        pre[0] = 1
        post[len(nums) - 1] = 1

        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
        
        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i + 1] * nums[i + 1]
        
        for i in range(len(nums)):
            result[i] = pre[i] * post[i]
        
        return result