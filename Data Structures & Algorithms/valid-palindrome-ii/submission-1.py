class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                
                l += 1
                r -= 1
            return True
            
        i = 0
        j = len(s) - 1

        if isPalindrome(i, j):
            return True
            
        while i <= j:
            if s[i] != s[j]:
                return isPalindrome(i + 1, j) or isPalindrome(i, j - 1)
            i += 1
            j -= 1
        
        return False
