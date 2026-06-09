class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        low = [0] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            
            if low[px] < low[py]:
                px, py = py, px
            parent[py] = px
            if low[px] == low[py]:
                low[px] += 1
            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]
        