class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for start, end in sorted(tickets)[::-1]:
            adj[start].append(end)
        
        result = []
        def dfs(node):
            while adj[node]:
                nxt = adj[node].pop()
                dfs(nxt)
            result.append(node)
        dfs("JFK")
        return result[::-1]
