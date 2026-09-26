class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = defaultdict(int)
        nums.sort()

        for num in nums:
            count[num] += 1

        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1

                if j - 1 > i and nums[j] == nums[j-1]:
                    continue
                
                want = -(nums[j] + nums[i])

                if count[want] > 0:
                    res.append([nums[i], nums[j], want])
            
            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1
        
        return res