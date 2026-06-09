class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = {i: [] for i in range(n)}
        for a, b in edges:
            d[a].append(b)
            d[b].append(a)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for n in d[node]:
                dfs(n)
            return

        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count



        