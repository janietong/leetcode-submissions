class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])

        def addFruit(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                return
            if grid[r][c] == 1:
                grid[r][c] = 2
                q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])

        while q:
            qLen = len(q)
            for _ in range(qLen):
                r, c = q.popleft()
                addFruit(r + 1, c)
                addFruit(r - 1, c)
                addFruit(r, c + 1)
                addFruit(r, c - 1)
            if len(q) > 0:
                minutes += 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return minutes
        
        