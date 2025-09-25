# Last updated: 9/24/2025, 9:35:41 PM
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        self.changeBorderCell(board)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"

    
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
    
    def backtrack(self, board, r, c, _from, _to):
        rows, cols = len(board), len(board[0])
        if r < 0 or r >= rows or c < 0 or c >= cols: return
        if board[r][c] != _from: return
        board[r][c] = _to
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            self.backtrack(board, r + dr, c + dc, _from, _to)
