class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        q = deque([])
        for r, char in enumerate(arr):
            q.append(char)
            if r - l >= k:
                if (abs(q[0] - x) > abs(char - x)):
                    q.popleft()
                else:
                    q.pop()
        return list(q)
            