class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1
        def palindrome(l, r):
            found = 0
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                found += 1
                l -= 1
                r += 1
            return found
        
        count = 0
        for i in range(len(s)):
            count += palindrome(i, i+1)
            count += palindrome(i, i)
        return count
        
    
                