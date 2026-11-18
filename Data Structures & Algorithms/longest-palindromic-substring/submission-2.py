class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i + 1:j]

        res = ""
        for i in range(len(s)):
            even = palindrome(i, i+1)
            odd = palindrome(i, i)

            if len(even) > len(res):
                res = even
            if len(odd) > len(res):
                res = odd
        return res