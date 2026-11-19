class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        def dfs(i, j, k):
            if k == len(s3):
                if i == len(s1) and j == len(s2):
                    return True
                return False
            
            if (i, j, k) in dp:
                return dp[(i, j, k)]
            
            res = False
            if i < len(s1) and s3[k] == s1[i]:
                res = res or dfs(i + 1, j, k + 1)
            if j < len(s2) and s3[k] == s2[j]:
                res = res or dfs(i, j + 1, k + 1)
            dp[(i, j, k)] = res
            return res
        return dfs(0, 0, 0)