class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = [(0, k)]
        adj = defaultdict(list)
        visited = set()

        for a, b, t in times:
            adj[a].append((b, t))
        
        minTime = 0
        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue 
            minTime = max(minTime, time)
            visited.add(node)

            if len(visited) == n:
                return minTime
            
            for nei, t in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap, (t + time, nei))
        
        return -1



        