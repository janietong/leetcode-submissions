class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        count = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        q = deque([])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))

        while q:
            qLen = len(q)
            for _ in range(qLen):
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr = dr + r
                    nc = dc + c
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            if q:
                count += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return count