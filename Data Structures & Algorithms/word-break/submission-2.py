class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]
            if i == len(s):
                return True
            
            res = False
            for j in range(i+1, len(s) + 1):
                if s[i:j] in wordSet and dfs(j):
                    res = True
            dp[i] = res
            return res
        return dfs(0)