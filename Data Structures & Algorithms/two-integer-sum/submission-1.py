class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            want = target - num
            if want in d:
                return [d[want], i]
            d[num] = i
