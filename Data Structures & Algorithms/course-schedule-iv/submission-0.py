class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        reach = {}
        def dfs(a):
            if a in reach:
                return reach[a]
            
            reach[a] = set()
            for c in graph[a]:
                reach[a].add(c)
                for child in dfs(c):
                    reach[a].add(child)
            
            return reach[a]

        
        for i in range(numCourses):
            dfs(i)
        
        return [b in reach[a] for a, b in queries]