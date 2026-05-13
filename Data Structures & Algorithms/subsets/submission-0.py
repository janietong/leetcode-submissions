class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            newSubset = []
            for subset in result:
                newSubset.append(subset + [num])
            result.extend(newSubset)
        return result