class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = {}

        def dfs(i, flag):
            if (i, flag) in dp:
                return dp[(i, flag)]
            
            if i == len(nums) - 1:
                if flag:
                    return max(0, nums[i])
                else:
                    return nums[i]
            
            if flag:
                dp[(i, flag)] = max(0, nums[i] + dfs(i+1, flag))
            else:
                dp[(i, flag)] = max(nums[i] + dfs(i+1, True), dfs(i+1, False))
            return dp[(i, flag)]
        
        return dfs(0, False)
