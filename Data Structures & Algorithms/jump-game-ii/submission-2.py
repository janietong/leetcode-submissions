class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        maxEnd = 0
        curEnd = 0

        for i in range(len(nums) - 1):
            maxEnd = max(maxEnd, i + nums[i])
            if i == curEnd:
                count += 1
                curEnd = maxEnd
        return count