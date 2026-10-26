class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        def reaches(node, target, seen):
            if node in seen:
                return False
            if node == target:
                return True
            seen.add(node)
            for c in graph[node]:
                if reaches(c, target, seen):
                    return True
            
            return False
        
        res = []

        for u, v in queries:
            if reaches(u, v, set()):
                res.append(True)
            else:
                res.append(False)
        return res