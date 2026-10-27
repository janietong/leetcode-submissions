class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[a].append(b)
        
        visiting = set()
        visited = set()

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
            return False
            
        for i in range(numCourses):
            if isCycle(i):
                return False
        return True
        