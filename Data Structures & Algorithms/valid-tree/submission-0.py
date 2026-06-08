class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        d = {i: [] for i in range(n)}

        for a, b in edges:
            d[a].append(b)
            d[b].append(a)

        visited = set()
        def cycle(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for n in d[node]:
                if n == prev:
                    continue
                if not cycle(n, node):
                    return False
            return True
        
        if not cycle(0, -1):
            return False
        
        return len(visited) == n