class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        leftMax = [-1] * n
        rightMax = [n] * n
        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMax[i] = stack[-1]
            stack.append(i)
        
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMax[i] = stack[-1]
            stack.append(i)
        
        maxLen = 0
        for i in range(n):
            leftMax[i] += 1
            rightMax[i] -= 1
            maxLen = max(maxLen, heights[i] * (rightMax[i] - leftMax[i] + 1))
        return maxLen