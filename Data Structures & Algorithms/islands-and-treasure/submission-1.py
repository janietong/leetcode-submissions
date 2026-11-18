class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque([])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
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
            count = 1
            for dr, dc in dirs:
                nr = dr + r
                nc = dc + c

                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF:
                    grid[nr][nc] = 1 + grid[r][c]
                    q.append((nr, nc))
