class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [float('inf')] * n
        edges = 0
        node = 0
        res = 0
        seen = set()

        while edges < n - 1:
            seen.add(node)
            nextNode = -1
            for i in range(n):
                if i not in seen:
                    curDist = abs(points[node][0] - points[i][0]) + abs(points[node][1] - points[i][1])
                    dist[i] = min(curDist, dist[i])

                    if nextNode == -1 or dist[i] < dist[nextNode]:
                        nextNode = i
            edges += 1
            node = nextNode
            res += dist[nextNode]
        return res