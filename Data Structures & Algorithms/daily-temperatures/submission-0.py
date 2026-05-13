class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, num in enumerate(temperatures):
            while stack and stack[-1][1] < num:
                ind, temp = stack.pop()
                result[ind] = i - ind
            stack.append((i, num))
        
        return result