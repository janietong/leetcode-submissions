class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        node = 0
        dist = [float('inf')] * n
        visited = [False] * n
        result = 0
        edges = 0

        while edges < n - 1:
            visited[node] = True
            nextNode = -1
            for i in range(n):
                if visited[i]:
                    continue
                curDist = abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1])

                dist[i] = min(dist[i], curDist)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i
            result += dist[nextNode]
            edges += 1
            node = nextNode
        
        return result
        