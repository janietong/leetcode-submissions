class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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

        count = 0
        for i in range(n):
            if i not in seen:
                count += 1
                dfs(i)
        return count