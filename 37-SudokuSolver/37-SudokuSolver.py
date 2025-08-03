# Last updated: 8/3/2025, 4:50:10 AM
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.found = False
        self.rows = [set() for i in range(9)]
        self.cols = [set() for i in range(9)]
        self.boxes = [set() for i in range(9)]
        self.initialize(board)
        startIndex = 0
        self.backtrack(startIndex, board)
    
    def initialize(self, board):
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                num = board[row][col]
                if num != '.':
                    self.rows[row].add(num)
                    self.cols[col].add(num)
                    self.boxes[self.getBoxIndex(row, col)].add(num)
    
    def getBoxIndex(self, row, col):
        return row // 3 * 3 + col // 3
    
    def backtrack(self, index, board):
        rows, cols = len(board), len(board[0])

        if self.found: return
        if index == rows * cols: 
            self.found = True
            return
        row = index // rows
        col = index % cols
        boxId = self.getBoxIndex(row, col)

        if board[row][col] != '.':
            self.backtrack(index + 1, board)
            return

        for num in '123456789':
            if not self.isValid(num, row, col, boxId):
                continue
            board[row][col] = num
            self.rows[row].add(num)
            self.cols[col].add(num)
            self.boxes[self.getBoxIndex(row, col)].add(num)
            
            self.backtrack(index + 1, board)
            if self.found: return
            
            board[row][col] = '.'
            self.rows[row].remove(num)
            self.cols[col].remove(num)
            self.boxes[self.getBoxIndex(row, col)].remove(num)
    
    def isValid(self, num, row, col, boxId):
        if num in self.rows[row]: return False
        if num in self.cols[col]: return False
        if num in self.boxes[boxId]: return False
        return True