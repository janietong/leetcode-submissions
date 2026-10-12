class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if "0000" in deadends:
            return -1
        
        def children(lock):
            res = []
            for i in range(len(target)):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res
        
        q = deque([("0000", 0)])
        seen = set(deadends)

        while q:
            lock, count = q.popleft()
            if lock == target:
                return count

            for child in children(lock):
                if child not in seen:
                    seen.add(child)
                    q.append((child, count + 1))
        return -1