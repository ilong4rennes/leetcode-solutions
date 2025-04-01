# Last updated: 3/31/2025, 11:50:06 PM
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1: return [[1]]
        M = [[0] * n for _ in range(n)]
        minRow, minCol, maxRow, maxCol = 0, 0, n - 1, n - 1
        num = 1
        while (minRow <= maxRow) and (minCol <= maxCol):
            for c in range(minCol, maxCol + 1):
                M[minRow][c] = num
                num += 1
            minRow += 1
            
            for r in range(minRow, maxRow + 1):
                M[r][maxCol] = num
                num += 1
            maxCol -= 1

            for c in range(maxCol, minCol - 1, -1):
                M[maxRow][c] = num
                num += 1
            maxRow -= 1

            for r in range(maxRow, minRow - 1, -1):
                M[r][minCol] = num 
                num += 1
            minCol += 1

        
        return M