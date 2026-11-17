class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur, seen):
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            
            for i in range(len(nums)):
                if i not in seen:
                    seen.add(i)
                    cur.append(nums[i])
                    dfs(cur, seen)
                    seen.remove(i)
                    cur.pop()
        
        dfs([], set())
        return res