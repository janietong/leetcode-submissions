class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        for s in strs[1:]:
            i = 0
            while i < min(len(res), len(s)):
                if s[i] != res[i]:
                    break
                i += 1
            res = s[:i]
        
        return res