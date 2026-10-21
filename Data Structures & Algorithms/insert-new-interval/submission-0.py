class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                return stack + [newInterval] + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                stack.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        stack.append(newInterval)
        return stack        