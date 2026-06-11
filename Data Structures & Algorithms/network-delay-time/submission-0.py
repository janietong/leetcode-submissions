class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
        
        heap = [(0, k)]
        result = 0
        visited = set()
        
        while heap:
            t, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            result = max(result, t)
            for nei, time in graph[node]:
                if nei not in visited:
                    heapq.heappush(heap, (time + t, nei))
        
        if len(visited) == n:
            return result
        return -1
