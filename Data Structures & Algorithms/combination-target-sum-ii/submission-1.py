class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def dfs(i, cur, total):
            if total > target or i > len(candidates):
                return
            if total == target:
                result.append(cur.copy())
                return
            
            prev = -1
            for j in range(i, len(candidates)):
                if candidates[j] == prev:
                    continue

                cur.append(candidates[j])
                dfs(j + 1, cur, total + candidates[j])
                cur.pop()

                prev = candidates[j]
        dfs(0, [], 0)
        return result
        