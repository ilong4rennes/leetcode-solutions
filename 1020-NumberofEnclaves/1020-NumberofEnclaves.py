# Last updated: 8/9/2025, 4:08:12 AM
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            if grid[row][0] == 1: self.dfs(row, 0, grid)
            if grid[row][cols - 1] == 1: self.dfs(row, cols - 1, grid)
        for col in range(cols):
            if grid[0][col] == 1: self.dfs(0, col, grid)
            if grid[rows - 1][col] == 1: self.dfs(rows - 1, col, grid)
        result = 0
        for row in range(1, rows - 1):
            for col in range(1, cols - 1):
                if grid[row][col] == 1:
                    result += 1
        return result
    
    def dfs(self, row, col, grid):
        rows, cols = len(grid), len(grid[0])
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return
        if grid[row][col] == 0:
            return
        grid[row][col] = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            newRow, newCol = row + dr, col + dc
            self.dfs(newRow, newCol, grid)