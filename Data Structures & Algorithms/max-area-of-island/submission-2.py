class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
            ROWS = len(grid)
            COLS = len(grid[0])

            seen = set()
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            res = 0
            def dfs(r, c):
                if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0 or (r, c) in seen:
                    return 0

                seen.add((r, c))
                count = 1
                for dr, dc in dirs:
                    nr = dr + r
                    nc = dc + c
                    count += dfs(nr, nc)
                
                return count

            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 1:
                        res = max(res, dfs(r, c))

            return res