class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}
        for c in t:
            d[c] = 1 + d.get(c, 0)
        
        window = {}
        have = 0
        l = 0
        need = len(d)
        resLen = float('inf')
        res = [-1, -1]

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in d and window[c] == d[c]:
                have += 1
            
            while need == have:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                
                window[s[l]] -= 1
                if s[l] in d and window[s[l]] < d[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float("inf") else ""
