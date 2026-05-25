class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(cur, i, curSum):
            if curSum == target:
                result.append(cur[:])
                return
            if i >= len(nums) or curSum > target:
                return
            
            cur.append(nums[i])
            dfs(cur, i, curSum + nums[i])
            cur.pop()
            dfs(cur, i + 1, curSum)
        dfs([], 0, 0)
        return result
        