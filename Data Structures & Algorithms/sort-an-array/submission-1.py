class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(a, b):
            i = 0
            j = 0
            res = []
            while i < len(a) and j < len(b):
                if a[i] <= b[j]:
                    res.append(a[i])
                    i += 1
                else:
                    res.append(b[j])
                    j += 1
            res.extend(a[i:])
            res.extend(b[j:])
            return res
        
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            m = len(arr) // 2
            return merge(mergeSort(arr[:m]), mergeSort(arr[m:]))
        return mergeSort(nums)