class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        d = {}
        for char in s1:
            d[char] = 1 + d.get(char, 0)
        
        l = 0
        for r in range(len(s2)):
            if s2[r] in d:
                d[s2[r]] -= 1
                while d[s2[r]] < 0:
                    d[s2[l]] += 1
                    l += 1
                
                if (r - l + 1) == len(s1):
                    return True
            else:
                while l < r:
                    d[s2[l]] += 1
                    l += 1
                l = r + 1
        
        return False