class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        stack = []
        for num in prices:
            if not stack or stack[-1][-1] > num:
                stack.append([num])
            else:
                stack[-1].append(num)

        res = 0
        for s in stack:
            res += s[-1] - s[0]
        return res