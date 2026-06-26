class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def dfs(nums):
            dp = {}
            def helper(i):
                n = len(nums)
                if i >= n:
                    return 0
                
                if i in dp:
                    return dp[i]

                dp[i] = max(helper(i + 1), nums[i] + helper(i + 2))
                return dp[i]
            return helper(0)

        return max(dfs(nums[:-1]), dfs(nums[1:]))