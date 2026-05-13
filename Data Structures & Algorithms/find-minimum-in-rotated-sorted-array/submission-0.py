class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        lowest = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                lowest = min(lowest, nums[l])
                break
            
            m = (l + r) // 2
            lowest = min(lowest, nums[m])

            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return lowest