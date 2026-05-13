class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            cur = [0] * 26
            for char in word:
                cur[ord(char) - ord('a')] += 1
            result[tuple(cur)].append(word)
        
        final = []
        for val in result.values():
            final.append(val)
        
        return final