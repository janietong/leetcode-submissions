class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        n = len(nums)
        for key, val in d.items():
            if n // 2 <= val:
                return key