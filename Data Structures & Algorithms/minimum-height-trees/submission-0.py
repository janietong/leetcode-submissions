class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        res = []
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        counts = [float('inf')] * n
        
        def dfs(node):
            seen.add(node)
            height = 0
            for nei in graph[node]:
                if nei not in seen:
                    height = max(height, 1 + dfs(nei))
            return height
        
        for i in range(n):
            seen = set()
            counts[i] = dfs(i)

        minNum = min(counts)
        for i, num in enumerate(counts):
            if num == minNum:
                res.append(i)
        return res