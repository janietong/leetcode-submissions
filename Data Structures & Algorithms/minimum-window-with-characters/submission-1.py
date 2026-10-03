class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        td = defaultdict(int)

        for char in t:
            td[char] += 1

        sd = defaultdict(int)

        l = 0
        required = len(td)
        formed = 0
        minLen = float('inf')
        minOption = ""

        for r in range(len(s)):
            c = s[r]
            sd[c] += 1

            if c in td and sd[c] == td[c]:
                formed += 1
            
            while required == formed:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    minOption = s[l:r+1]
                
                leftChar = s[l]
                sd[leftChar] -= 1

                if leftChar in td and sd[leftChar] < td[leftChar]:
                    formed -= 1
                l += 1
        
        return minOption