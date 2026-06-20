class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}
        for start, end, t in times:
            adj[start].append((t, end))
        
        visited = set()
        heap = [(0, k)]
        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return time
            for t, end in adj[node]:
                if end not in visited:
                    heapq.heappush(heap, (time + t, end))
        return -1
