class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def dfs(cur, i):
            if i >= len(nums):
                result.append(cur[:])
                return
            
            cur.append(nums[i])
            dfs(cur, i + 1)
            cur.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(cur, i + 1)
        
        dfs([], 0)
        return result
        