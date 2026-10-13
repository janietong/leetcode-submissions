class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        children = {}

        for a, b in prerequisites:
            graph[a].append(b)
        
        def dfs(node):
            if node in children:
                return children[node]
            children[node] = set()

            for child in graph[node]:
                children[node].add(child)

                for c in dfs(child):
                    children[node].add(c)
            
            return children[node]
        
        for i in range(numCourses):
            dfs(i)
        
        res = []
        for a, b in queries:
            if b in children[a]:
                res.append(True)
            else:
                res.append(False)
        
        return res
        