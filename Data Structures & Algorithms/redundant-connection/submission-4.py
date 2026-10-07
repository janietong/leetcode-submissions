class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        n = len(edges)
        indegree = [0] * (n+1)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
        
        q = deque([])
        for i in range(1, n+1):
            if indegree[i] == 1:
                q.append(i)
        
        while q:
            node = q.popleft()
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append(nei)
        
        for a, b in reversed(edges):
            if indegree[b] == 2 and indegree[a] == 2:
                return [a, b]
        return []

        