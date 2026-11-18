class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in dp:
                return dp[i]

            cur = nums[i] + dfs(i + 2)
            cur = max(cur, dfs(i + 1))
            dp[i] = cur
            return cur
        return dfs(0)