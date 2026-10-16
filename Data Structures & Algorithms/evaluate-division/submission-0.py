class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            val = values[i]
            graph[a].append((b, val))
            graph[b].append((a, 1/val))
        
        res = []
        for src, dst in queries:
            if src not in graph or dst not in graph:
                res.append(-1)
                continue

            seen = set()
            ans = -1
            q = deque([(src, 1)])

            while q:
                node, w = q.popleft()
                if node in seen:
                    continue
                
                seen.add(node)
                if node == dst:
                    ans = w
                    break
                
                for nei, weight in graph[node]:
                    if nei not in seen:
                        q.append((nei, weight * w))
            
            res.append(ans)
        return res