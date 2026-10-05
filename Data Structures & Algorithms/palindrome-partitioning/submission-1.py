class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(sub):
            l = 0
            r = len(sub) - 1
            while l <= r:
                if sub[l] != sub[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def dfs(i, cur):
            if i >= len(s):
                res.append(cur[:])
                return
            
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]
                if isPalindrome(sub):
                    cur.append(sub)
                    dfs(j, cur)
                    cur.pop()
        
        dfs(0, [])
        return res
