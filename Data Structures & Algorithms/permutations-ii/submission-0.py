class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = set()

        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            
            for j in range(len(nums)):
                if j in used:
                    continue
                if j > 0 and nums[j-1] == nums[j] and (j-1) not in used:
                    continue
                used.add(j)
                cur.append(nums[j])
                dfs(cur)
                cur.pop()
                used.remove(j)
        
        dfs([])
        return res