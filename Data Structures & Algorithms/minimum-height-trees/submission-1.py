class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
            
        graph = defaultdict(list)
        indegree = [0] * n
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] += 1

        q = deque([])
        remaining = n
        for i in range(n):
            if indegree[i] == 1:
                q.append(i)
        
        while q:
            if remaining <= 2:
                return list(q)
            remaining -= len(q)
            for _ in range(len(q)):
                node = q.popleft()
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        q.append(nei)
        return []
