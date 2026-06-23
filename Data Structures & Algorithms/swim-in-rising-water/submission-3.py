class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)]
        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()

        while heap:
            time, r, c = heapq.heappop(heap)
            if r == ROWS - 1 and c == COLS - 1:
                return time
            if (r, c) in visited:
                continue
            visited.add((r, c))
            for dr, dc in dirs:
                nr = dr + r
                nc = dc + c
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    if (nr, nc) not in visited:
                        heapq.heappush(heap, (max(time, grid[nr][nc]), nr, nc))
        return -1