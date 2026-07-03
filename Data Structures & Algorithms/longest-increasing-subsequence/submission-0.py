class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [-1] * (len(nums) + 1)
        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            dp[i] = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dfs(j))
            return dp[i]
        return max(dfs(i) for i in range(len(nums)))