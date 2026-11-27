class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [float('inf')] * n
        seen = set()
        res = 0
        node = 0
        edges = 0

        while edges < n - 1:
            seen.add(node)
            nextNode = -1
            for i in range(n):
                if i not in seen:
                    curDist = abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1])
                    dist[i] = min(dist[i], curDist)

                    if nextNode == -1 or dist[i] < dist[nextNode]:
                        nextNode = i
            node = nextNode
            edges += 1
            res += dist[nextNode]
        return res