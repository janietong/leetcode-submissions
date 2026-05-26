class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(seen, cur):
            if len(cur) == len(nums):
                result.append(cur[:])
                return
            
            for i in range(len(nums)):
                if i not in seen:
                    cur.append(nums[i])
                    seen.add(i)
                    dfs(seen, cur)
                    cur.pop()
                    seen.remove(i)
        
        dfs(set(), [])
        return result
        