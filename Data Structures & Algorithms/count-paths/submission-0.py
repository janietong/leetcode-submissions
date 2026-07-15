class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        dirs = [(0, 1), (1, 0)]

        def dfs(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            if (r, c) in dp:
                return dp[(r, c)]
            if r >= m or c >= n:
                return 0
            
            count = 0
            for dr, dc in dirs:
                nr = dr + r
                nc = dc + c
                count += dfs(nr, nc)
            dp[(r, c)] = count
            return count
        return dfs(0, 0)
            

            