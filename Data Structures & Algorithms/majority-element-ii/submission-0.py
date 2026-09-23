class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        d = defaultdict(int)
        n = len(nums)
        seen = set()

        for num in nums:
            d[num] += 1
        
        for key, count in d.items():
            if count > (n // 3):
                if key not in seen:
                    res.append(key)
                    seen.add(key)
        
        return res