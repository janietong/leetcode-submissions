class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pac = set()
        atl = set()
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r, c, ocean, prevHeight):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in ocean or heights[r][c] < prevHeight:
                return

            ocean.add((r, c))
            for dr, dc in dirs:
                nr = dr + r
                nc = dc + c
                dfs(nr, nc, ocean, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
        res = set()
        for val in pac:
            if val in atl:
                res.add(val)

        for val in atl:
            if val in pac:
                res.add(val)

        return list(res)