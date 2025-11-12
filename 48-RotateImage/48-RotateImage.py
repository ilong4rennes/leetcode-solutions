# Last updated: 11/12/2025, 11:10:47 AM
class Solution:
    def diagonalFlip(self, matrix):
        n = len(matrix)
        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        return matrix

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix = self.diagonalFlip(matrix)
        for row in range(n):
            matrix[row].reverse()