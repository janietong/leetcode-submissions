class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[b].append(a)
        
        seen = set()
        visiting = set()
        def isCycle(node):
            if node in seen:
                return False
            if node in visiting:
                return True
            
            visiting.add(node)
            for nei in graph[node]:
                if isCycle(nei):
                    return True
            visiting.remove(node)
            seen.add(node)
            return False
        
        for i in range(numCourses):
            if isCycle(i):
                return False
        
        return True