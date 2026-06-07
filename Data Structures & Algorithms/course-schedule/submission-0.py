class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {i: [] for i in range(numCourses)}
        visited = set()
        for a, b in prerequisites:
            d[a].append(b)
        
        def dfs(course):
            if course in visited:
                return False
            if d[course] == []:
                return True
            
            visited.add(course)
            for c in d[course]:
                if not dfs(c):
                    return False
            visited.remove(course)
            d[course] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        