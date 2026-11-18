class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen = set(deadends)
        if target in seen or "0000" in seen:
            return -1
        
        def child(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res
        
        q = deque([("0000", 0)])
        while q:
            val, count = q.popleft()
            if val == target:
                return count
            if val in seen:
                continue
            seen.add(val)
            for c in child(val):
                q.append((c, count + 1))
        return -1