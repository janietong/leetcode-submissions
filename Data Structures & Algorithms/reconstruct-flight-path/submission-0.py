class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        fromTo = defaultdict(list)
        for start, end in sorted(tickets)[::-1]:
            fromTo[start].append(end)
        
        result = []
        def dfs(node):
            while fromTo[node]:
                dst = fromTo[node].pop()
                dfs(dst)
            result.append(node)
        dfs('JFK')
        return result[::-1]
        

        