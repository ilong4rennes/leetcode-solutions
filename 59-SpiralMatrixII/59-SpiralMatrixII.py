# Last updated: 11/12/2025, 9:00:19 PM
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        num = 1
        upper, lower = 0, n - 1
        left, right = 0, n - 1

        while num <= n * n:
            for col in range(left, right + 1):
                matrix[upper][col] = num
                num += 1
            upper += 1

            for row in range(upper, lower + 1):
                matrix[row][right] = num
                num += 1
            right -= 1

            for col in range(right, left - 1, -1):
                matrix[lower][col] = num
                num += 1
            lower -= 1

            for row in range(lower, upper - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1

        return matrix                