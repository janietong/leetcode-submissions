class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [float('inf')] * n
        seen = set()

        edges = 0
        node = 0
        res = 0

        while edges < n-1:
            seen.add(node)
            nextNode = -1
            for i in range(n):
                if i not in seen:
                    cur = abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1])
                    dist[i] = min(dist[i], cur)

                    if nextNode == -1 or dist[i] < dist[nextNode]:
                        nextNode = i
            res += dist[nextNode]
            node = nextNode
            edges += 1
        return res