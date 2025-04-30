# Last updated: 4/30/2025, 2:32:11 AM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1
        row = 0
        while top <= bot:
            mid = (top + bot) // 2
            currNum = matrix[mid][0]
            if currNum == target: return True
            elif currNum < target:
                row = mid
                top = mid + 1
            else: # currNum > target
                bot = mid - 1
        
        left, right = 0, cols - 1
        while left <= right:
            mid = (left + right) // 2
            currNum = matrix[row][mid]
            if currNum == target: return True
            elif currNum < target:
                left = mid + 1
            else:
                right = mid - 1
        return False