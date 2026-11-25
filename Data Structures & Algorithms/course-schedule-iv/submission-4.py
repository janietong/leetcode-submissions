class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[b].append(a)

        def canReach(u, v):
            seen.add(u)
            for nei in graph[u]:
                if nei == v:
                    return True
                if nei in seen:
                    continue
                if canReach(nei, v):
                    return True
            return False
            
        res = []
        for a, b in queries:
            seen = set()
            res.append(canReach(b, a))
        return res