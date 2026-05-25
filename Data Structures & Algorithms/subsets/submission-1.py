class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(cur, i):
            if i >= len(nums):
                result.append(cur[:])
                return
            
            cur.append(nums[i])
            dfs(cur, i + 1)
            cur.pop()
            dfs(cur, i + 1)
        dfs([], 0)
        return result