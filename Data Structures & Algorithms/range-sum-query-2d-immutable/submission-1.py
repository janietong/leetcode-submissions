class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        self.matrixSum = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            cur = 0
            for c in range(COLS):
                cur += matrix[r][c]
                above = self.matrixSum[r][c+1]
                self.matrixSum[r+1][c+1] = cur + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        topLeft = self.matrixSum[row1-1][col1 - 1]
        left = self.matrixSum[row2][col1-1]
        top = self.matrixSum[row1-1][col2]
        bottomRight = self.matrixSum[row2][col2]
        return bottomRight - top - left + topLeft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)