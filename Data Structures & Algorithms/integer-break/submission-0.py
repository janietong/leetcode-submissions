class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            maxSoFar = 0
            for j in range(1, i):
                maxSoFar = max(maxSoFar, j * (i - j), j * dfs(i - j))
            
            dp[i] = maxSoFar
            return maxSoFar
        return dfs(n)
            