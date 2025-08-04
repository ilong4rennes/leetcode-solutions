# Last updated: 8/4/2025, 3:10:55 AM
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.result = 0
        self.board = ['.' * n for _ in range(n)]
        startRow = 0
        self.backtrack(startRow, n)
        return self.result
    
    def backtrack(self, row, n):
        if row == n:
            self.result += 1
            return
        for col in range(n):
            if not self.isValid(row, col, n):
                continue
            self.board[row] = self.board[row][:col] + 'Q' + self.board[row][col + 1:]
            self.backtrack(row + 1, n)
            self.board[row] = self.board[row][:col] + '.' + self.board[row][col + 1:]
    
    def isValid(self, row, col, n):
        # Check col
        for r in range(row):
            if self.board[r][col] != '.': return False

        # Check upper left
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if self.board[r][c] != '.': return False
            r, c = r - 1, c - 1

        # Check upper right
        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if self.board[r][c] != '.': return False
            r, c = r - 1, c + 1
        
        return True