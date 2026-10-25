class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxSoFar = 0
        cur = 0
        for i in range(1, len(arr) - 1):
            a, b, c = arr[i-1], arr[i], arr[i+1]
            if (a < b and c < b) or (a > b and c > b):
                cur += 1
            else:
                cur = 0
            maxSoFar = max(cur, maxSoFar)
        
        if maxSoFar:
            return maxSoFar + 2
        return 2 if any(arr[i] != arr[i+1] for i in range(len(arr) - 1)) else 1