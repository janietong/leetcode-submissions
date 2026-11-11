class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numSet = set(nums)

        for num in numSet:
            if num - 1 not in numSet:
                cur = 1
                while cur + num in numSet:
                    cur += 1
                res = max(res, cur)
        return res
        