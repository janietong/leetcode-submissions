class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW = len(matrix)
        COL = len(matrix[0])
        t = 0
        b = ROW - 1

        while t <= b:
            row = (t + b) // 2
            if matrix[row][0] > target:
                b = row - 1
            elif matrix[row][-1] < target:
                t = row + 1
            else:
                break
        
        if not (t <= b):
            return False
        row = (t + b) // 2

        l = 0
        r = COL - 1
        while l <= r:
            col = (l + r) // 2
            if matrix[row][col] < target:
                l = col + 1
            elif matrix[row][col] > target:
                r = col - 1
            else:
                return True
        return False
        