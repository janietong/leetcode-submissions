class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        i = 0
        minVal = min(nums)
        maxVal = max(nums)
        for val in range(minVal, maxVal + 1):
            while count[val] > 0:
                count[val] -= 1
                nums[i] = val
                i += 1
        return nums
