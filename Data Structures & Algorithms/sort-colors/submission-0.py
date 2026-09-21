class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        minN = min(nums)
        maxN = max(nums)

        i = 0
        for val in range(minN, maxN + 1):
            while count[val] > 0:
                count[val] -= 1
                nums[i] = val
                i += 1
        
        return nums