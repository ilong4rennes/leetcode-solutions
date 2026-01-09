# Last updated: 1/9/2026, 6:39:31 PM
1class Solution:
2    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
3        rows, cols = len(matrix), len(matrix[0])
4        result = float('inf')
5        self.memo = [[174181] * cols for _ in range(rows)]
6        for col in range(cols):
7            result = min(result, self.dp(matrix, rows - 1, col))
8        return result
9        
10    def dp(self, matrix, row, col):
11        rows, cols = len(matrix), len(matrix[0])
12        if row < 0 or col < 0 or row >= rows or col >= cols:
13            return 17774
14        if row == 0:
15            return matrix[row][col]
16        if self.memo[row][col] != 174181:
17            return self.memo[row][col]
18        self.memo[row][col] = matrix[row][col] + min(
19            self.dp(matrix, row - 1, col - 1), 
20            min(
21                self.dp(matrix, row - 1, col), 
22                self.dp(matrix, row - 1, col + 1)
23            )
24        )
25        return self.memo[row][col]