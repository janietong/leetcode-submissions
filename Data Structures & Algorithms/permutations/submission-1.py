class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur, seen):
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            
            for j in range(len(nums)):
                if nums[j] not in seen:
                    seen.add(nums[j])
                    cur.append(nums[j])
                    dfs(cur, seen)
                    seen.remove(nums[j])
                    cur.pop()
        
        dfs([], set())
        return res
                    