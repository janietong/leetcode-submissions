class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)
        for char in s:
            d[char] = d.get(char, 0) + 1
        
        for char in t:
            if char in d:
                d[char] -= 1
            else:
                return False
        
        for val in d.values():
            if val != 0:
                return False
        
        return True