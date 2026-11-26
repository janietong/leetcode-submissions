class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        res = []
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[b].append(a)

        def dfs(u, v):
            if u == v:
                return True
            seen.add(u)
            for nei in graph[u]:
                if nei not in seen:
                    if dfs(nei, v):
                        return True
            return False
        
        for a, b in queries:
            seen = set()
            res.append(dfs(b, a))
        return res