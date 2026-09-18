class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word)) + "#" + word
        return s

    def decode(self, s: str) -> List[str]:
        strArr = []
        n = len(s)
        i = 0

        while i < n:
            j = i
            while s[j] != "#":
                j += 1
            l = int(s[i:j])
            i = j + 1
            j = i + l
            strArr.append(s[i:j])
            i = j

        return strArr
