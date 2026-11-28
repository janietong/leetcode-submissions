class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        want = total // 2
        dp = {}
        def dfs(i, target):
            if i == len(nums):
                return target == 0
            if (i, target) in dp:
                return dp[(i, target)]
            if target < 0:
                return False
            res = dfs(i+1, target) or dfs(i+1, target-nums[i])
            dp[(i, target)] = res
            return res
        return dfs(0, want)