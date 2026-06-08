class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        result = []
        d = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            d[a].append(b)
        
        def dfs(c):
            if c in visited:
                return False
            if d[c] == []:
                if c not in result:
                    result.append(c)
                return True
            
            visited.add(c)
            for n in d[c]:
                if not dfs(n):
                    return False
            visited.remove(c)
            d[c] = []
            result.append(c)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []

        return result
            
        