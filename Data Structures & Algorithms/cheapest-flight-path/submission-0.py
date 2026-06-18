class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d = {i : [] for i in range(n)}
        for start, end, price in flights:
            d[start].append((end, price))

        minHeap = [(0, 0, src)] # cost, stops, node

        visited = {}
        while minHeap :
            price, stops, node = heapq.heappop(minHeap)
            if node == dst:
                return price
            if stops > k:
                continue
            if node in visited and visited[node] <= stops:
                continue
            visited[node] = stops

            for nei, p in d[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (price + p, stops + 1, nei))
        return -1 
            
