class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        minNum = min(nums)
        maxNum = max(nums)
        i = 0
        for num in range(minNum, maxNum + 1):
            while count[num] > 0:
                count[num] -= 1
                nums[i] = num
                i += 1
        
        