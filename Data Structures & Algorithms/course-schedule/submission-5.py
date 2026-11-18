class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        visiting = set()
        visited = set()

        def isCycle(i):
            if i in visited:
                return False
            if i in visiting:
                return True
            
            visiting.add(i)
            for nei in graph[i]:
                if isCycle(nei):
                    return True
            visiting.remove(i)
            visited.add(i)
            return False
        
        for i in range(numCourses):
            if isCycle(i):
                return False
        return True