class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows, cols = len(maze), len(maze[0])
        visited = dict()
        for row in range(rows):
            for col in range(cols):
                visited[(row, col)] = False
        stack = deque()
        stack.append(tuple(start))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while stack:
            curr_row, curr_col = stack.pop()
            if curr_row == destination[0] and curr_col == destination[1]:
                return True
            for dr, dc in directions:
                next_row, next_col = curr_row, curr_col
                while (0 <= next_row + dr < rows and 
                       0 <= next_col + dc < cols and
                       maze[next_row + dr][next_col + dc] == 0):
                    next_row += dr
                    next_col += dc
                if (not visited[(next_row, next_col)]):
                    stack.append((next_row, next_col))
                    visited[(next_row, next_col)] = True
        return False