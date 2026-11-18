class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            cur = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    cur = max(cur, 1 + dfs(j))
            dp[i] = cur
            return cur
        return max(dfs(i) for i in range(len(nums)))
 