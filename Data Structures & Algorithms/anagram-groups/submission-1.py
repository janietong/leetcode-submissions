class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char.lower()) - 97] += 1
            d[tuple(key)].append(word)
        res = []
        for val in d.values():
            res.append(val)
        return res