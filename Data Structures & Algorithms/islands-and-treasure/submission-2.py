class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return []
        
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q = deque([])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        seen = set()
        while q:
            r, c = q.popleft()
            if (r, c) in seen:
                continue

            seen.add((r, c))
            for dr, dc in dirs:
                nr = dr + r
                nc = dc + c
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF:
                    grid[nr][nc] = 1 + grid[r][c]
                    q.append((nr, nc))