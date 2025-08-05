# Last updated: 8/5/2025, 4:49:03 AM
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] == 1 and grid1[row][col] == 0: 
                    self.dfs(row, col, grid2)

        result = 0 
        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] == 1:
                    result += 1
                    self.dfs(row, col, grid2)
        
        return result
    
    def dfs(self, row, col, grid):
        rows, cols = len(grid), len(grid[0])
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return
        if grid[row][col] == 0:
            return
        grid[row][col] = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            newRow, newCol = row + dr, col + dc
            self.dfs(newRow, newCol, grid)