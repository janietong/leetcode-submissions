class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        seen = {}
        maxLen = 0
        res = 0

        for r in range(len(s)):
            seen[s[r]] = 1 + seen.get(s[r], 0)
            maxLen = max(maxLen, seen[s[r]])

            while (r - l + 1) - maxLen > k:
                seen[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res