class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        ds1 = defaultdict(int)

        for char in s1:
            ds1[char] += 1
        n = len(s1)

        l = 0
        ds2 = defaultdict(int)

        for r in range(len(s2)):
            ds2[s2[r]] += 1
            while r - l + 1 > n:
                leftChar = s2[l]
                ds2[leftChar] -= 1

                if ds2[leftChar] == 0:
                    del ds2[leftChar]
                l += 1
            if ds2 == ds1:
                return True
        return False
                