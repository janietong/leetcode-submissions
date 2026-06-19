class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = defaultdict(list)
        for a, b in prerequisites:
            preReq[a].append(b)
        
        visited = set()
        completed = set()
        def cycle(node):
            if node in visited:
                return True
            if node in completed:
                return False
            visited.add(node)
            for nei in preReq[node]:
                if cycle(nei):
                    return True
            visited.remove(node)
            completed.add(node)
            return False
        
        for i in range(numCourses):
            if cycle(i):
                return False
        return True
        