# Last updated: 8/4/2025, 11:48:29 PM
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.image = image
        originalColor = image[sr][sc]
        if originalColor == color: return image
        self.dfs(sr, sc, originalColor, color)
        return self.image

    def dfs(self, row, col, originalColor, color):
        rows, cols = len(self.image), len(self.image[0])
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return
        if self.image[row][col] != originalColor:
            return
        self.image[row][col] = color
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            newRow, newCol = row + dr, col + dc
            self.dfs(newRow, newCol, originalColor, color)