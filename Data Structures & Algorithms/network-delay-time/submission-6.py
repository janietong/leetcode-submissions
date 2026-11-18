class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append((v, t))
        
        seen = set()
        heap = [[0, k]]

        heapq.heapify(heap)

        while heap:
            count, node = heapq.heappop(heap)
            if node in seen:
                continue
            seen.add(node)
            if len(seen) == n:
                return count
            seen.add(node)
            for nei, t in graph[node]:
                heapq.heappush(heap, [count + t, nei])
        return -1