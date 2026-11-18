class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dfs(arr):
            dp = {}
            def helper(i):
                if i >= len(arr):
                    return 0
                if i in dp:
                    return dp[i]
                
                dp[i] = max(arr[i] + helper(i + 2), helper(i + 1))
                return dp[i]
            return helper(0)
        return max(dfs(nums[:-1]), dfs(nums[1:]))