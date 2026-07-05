class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(amt):   
            if amt == 0:
                return 0
            if amt in dp:
                return dp[amt]
            result = float('inf')
            for c in coins:
                if amt - c >= 0:
                    result = min(result, 1 + dfs(amt - c))
            dp[amt] = result
            return result
        result = dfs(amount)
        if result == float('inf'):
            return -1
        return result