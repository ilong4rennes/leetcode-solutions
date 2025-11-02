# Last updated: 11/2/2025, 3:07:19 PM
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.preSum = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        # Populate 2D preSum array
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                self.preSum[row][col] = (matrix[row-1][col-1] + self.preSum[row][col-1]
                                 + self.preSum[row-1][col] - self.preSum[row-1][col-1])
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.preSum[row2+1][col2+1] - self.preSum[row2+1][col1] - self.preSum[row1][col2+1] + self.preSum[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)