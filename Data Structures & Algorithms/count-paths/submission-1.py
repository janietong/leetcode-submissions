class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def dfs(r, c):
            if r < 0 or r == m or c < 0 or c == n:
                return 0
            
            if r == m - 1 and c == n - 1:
                return 1

            if (r, c) in dp:
                return dp[(r, c)]
            
            count = dfs(r + 1, c)
            count += dfs(r, c + 1)
            dp[(r, c)] = count
            return count
        return dfs(0, 0)