class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append((v, t))
        
        heap = [(0, k)]
        seen = set()

        while heap:
            time, node = heapq.heappop(heap)
            if node in seen:
                continue
            seen.add(node)
            if len(seen) == n:
                return time
            for nei, t in graph[node]:
                heapq.heappush(heap, (t + time, nei))
        
        return -1