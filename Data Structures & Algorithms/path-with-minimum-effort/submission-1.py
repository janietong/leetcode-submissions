class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS = len(heights)
        COLS = len(heights[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seen = set()
        heap = [(0, 0, 0)]

        while heap:
            effort, r, c = heapq.heappop(heap)
            if (r, c) in seen:
                continue
            seen.add((r, c))
            if r == ROWS - 1 and c == COLS - 1:
                return effort
            
            for dr, dc in dirs:
                nr = dr + r
                nc = dc + c
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in seen:
                    continue
                heapq.heappush(heap, (max(effort, abs(heights[r][c] - heights[nr][nc])), nr, nc))