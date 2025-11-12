# Last updated: 11/12/2025, 12:28:51 PM
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        result = []
        upper, lower = 0, rows - 1
        left, right = 0, cols - 1
        while len(result) < rows * cols:
            if upper <= lower:
                for col in range(left, right + 1):
                    result.append(matrix[upper][col])
                upper += 1
            if left <= right:
                for row in range(upper, lower + 1):
                    result.append(matrix[row][right])
                right -= 1
            if upper <= lower:
                for col in range(right, left - 1, -1):
                    result.append(matrix[lower][col])
                lower -= 1
            if left <= right:
                for row in range(lower, upper - 1, -1):
                    result.append(matrix[row][left])
                left += 1
        return result