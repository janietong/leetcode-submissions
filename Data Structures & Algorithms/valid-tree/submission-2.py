class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set()

        def isCycle(node, parent):
            seen.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if nei in seen:
                    return True
                if isCycle(nei, node):
                    return True
            return False

        if isCycle(0, -1):
            return False
        return len(seen) == n