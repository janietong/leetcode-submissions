class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minLen = min(len(word1), len(word2))

        s = ""

        for i in range(minLen):
            s += word1[i]
            s += word2[i]
        
        if len(word2) > len(word1):
            s += word2[minLen:]
        elif len(word1) > len(word2):
            s += word1[minLen:]

        return s