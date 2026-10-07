class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for a, b, t in times:
            graph[a].append((t, b))
        
        t = 0
        heap = [(0, k)]
        seen = set()

        while heap:
            time, node = heapq.heappop(heap)
            if node in seen:
                continue
            seen.add(node)
            t = time
            for nt, nei in graph[node]:
                if nei not in seen:
                    heapq.heappush(heap, (nt + t, nei))
        
        return t if len(seen) == n else -1