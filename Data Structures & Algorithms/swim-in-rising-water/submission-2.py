class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [(grid[0][0], 0, 0)]
        visited = set()
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ROWS = len(grid)
        COLS = len(grid[0])

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == ROWS - 1 and c == COLS - 1:
                return t
            if (r, c) in visited:
                continue
            visited.add((r, c))
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    if (nr, nc) not in visited:
                        heapq.heappush(minHeap, (max(t,grid[nr][nc]), nr, nc))
        return -1