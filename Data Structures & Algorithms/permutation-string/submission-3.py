class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = Counter(s1)
        n = len(s1)

        d2 = Counter()
        for r, ch in enumerate(s2):
            d2[ch] += 1
            if r >= n:
                leftChar = s2[r - n]
                d2[leftChar] -= 1
                if d2[leftChar] <= 0:
                    del d2[leftChar]
            
            if d == d2:
                return True
        return False