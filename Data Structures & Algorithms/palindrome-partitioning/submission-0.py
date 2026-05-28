class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def isPalindrome(subs):
            l = 0
            r = len(subs) - 1

            while l <= r:
                if subs[l] != subs[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def dfs(cur, i):
            if i >= len(s):
                result.append(cur[:])
                return
            
            for j in range(i, len(s)):
                subs = s[i:j + 1]
                if isPalindrome(subs):
                    cur.append(subs)
                    dfs(cur, j + 1)
                    cur.pop()
        
        dfs([], 0)
        return result