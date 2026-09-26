class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        i = 0
        j = len(s) - 1

        while i < j:
            a = s[i]
            b = s[j]

            s[i] = b
            s[j] = a

            i += 1
            j -= 1
        
        return s
        