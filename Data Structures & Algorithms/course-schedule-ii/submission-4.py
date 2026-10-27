class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[a].append(b)
        
        visiting = set()
        visited = set()
        res = []
        def isCycle(node):
            if node in visiting:
                return True
            if node in visited:
                return False
            
            visiting.add(node)

            for nei in graph[node]:
                if isCycle(nei):
                    return True
            
            visiting.remove(node)
            visited.add(node)
            res.append(node)
            return False
        
        for i in range(numCourses):
            if isCycle(i):
                return []
        return res