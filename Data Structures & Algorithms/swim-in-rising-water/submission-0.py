class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while heap:
            time, r, c = heapq.heappop(heap)
            if r == ROWS - 1 and c == COLS - 1:
                return time
            if (r, c) in visited:
                continue
            visited.add((r, c))
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in visited:
                    continue
                heapq.heappush(heap, (max(time, grid[nr][nc]), nr, nc))
        return -1
        