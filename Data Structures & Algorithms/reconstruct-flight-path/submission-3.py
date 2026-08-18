class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            adj[a].append(b)

        result = []

        def dfs(node):
            while adj[node]:
                nxt = adj[node].pop()
                dfs(nxt)
            result.append(node)
        
        dfs("JFK")
        return result[::-1]


