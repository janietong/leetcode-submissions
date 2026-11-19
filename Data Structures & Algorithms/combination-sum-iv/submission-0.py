class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        nums.sort()

        def dfs(want):
            if want in dp:
                return dp[want]
            count = 0
            for num in nums:
                if want < num:
                    continue
                count += dfs(want-num)
            dp[want] = count
            return count
        return dfs(target)