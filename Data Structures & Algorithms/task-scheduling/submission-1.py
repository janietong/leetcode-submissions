class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        time = 0
        q = deque()
        heap = [-val for val in count.values()]
        heapq.heapify(heap)

        while heap or q:
            time += 1
            if not heap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0]) 
        return time       