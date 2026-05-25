class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def dfs(cur, i, curSum):
            if curSum == target:
                result.append(cur[:])
                return
            
            if i >= len(candidates) or curSum > target:
                return
            
            cur.append(candidates[i])
            dfs(cur, i + 1, curSum + candidates[i])
            cur.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(cur, i + 1, curSum)
        
        dfs([], 0, 0)
        return result
        