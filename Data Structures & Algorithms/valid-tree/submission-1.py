class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set()
        def dfs(node):
            if node in seen:
                return 
            
            seen.add(node)
            for nei in graph[node]:
                dfs(nei)
            
        dfs(0)
        return len(seen) == n
        