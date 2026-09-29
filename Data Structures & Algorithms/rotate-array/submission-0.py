class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        rotate = k % n

        nums[:] = nums[-rotate:] + nums[:-rotate]
        return nums