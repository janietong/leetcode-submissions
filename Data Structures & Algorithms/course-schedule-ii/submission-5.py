class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        visiting = set()
        visited = set()
        res = []

        def isCycle(i):
            if i in visiting:
                return True
            if i in visited:
                return False
            
            visiting.add(i)
            for nei in graph[i]:
                if isCycle(nei):
                    return True
            res.append(i)
            visiting.remove(i)
            visited.add(i)
            return False
        for i in range(numCourses):
            if isCycle(i):
                return []
        return res