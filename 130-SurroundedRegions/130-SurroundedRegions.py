# Last updated: 9/24/2025, 9:31:06 PM
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.changeBorderCell(board)
        self.replaceCell(board, "O", "O", "X")
        self.replaceCell(board, "#", "#", "O")
    
    def changeBorderCell(self, board):
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            if board[row][0] == "O":
                self.backtrack(board, row, 0, "O", "#")
            if board[row][cols - 1] == "O":
                self.backtrack(board, row, cols - 1, "O", "#")
        for col in range(cols):
            if board[0][col] == "O":
                self.backtrack(board, 0, col, "O", "#")  
            if board[rows - 1][col] == "O":
                self.backtrack(board, rows - 1, col, "O", "#")
    
    def replaceCell(self, board, orig, _from, _to):
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == orig:
                    self.backtrack(board, row, col, _from, _to)
    
    def backtrack(self, board, r, c, _from, _to):
        rows, cols = len(board), len(board[0])
        if r < 0 or r >= rows or c < 0 or c >= cols: return
        if board[r][c] != _from: return
        board[r][c] = _to
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            self.backtrack(board, r + dr, c + dc, _from, _to)
