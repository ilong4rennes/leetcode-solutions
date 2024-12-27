class Solution:
    def shortestDistance(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        visited = {}
        for row in range(rows):
            for col in range(cols):
                visited[(row, col)] = float('inf')
        visited[tuple(ball)] = 0
        stack = deque()
        stack.append((ball[0], ball[1], 0))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while stack:
            curr_row, curr_col, dist = stack.pop()
            for dr, dc in directions:
                next_row, next_col, next_dist = curr_row, curr_col, dist
                while (0 <= next_row + dr < rows and
                       0 <= next_col + dc < cols and
                       maze[next_row + dr][next_col + dc] == 0):
                       next_row += dr
                       next_col += dc
                       next_dist += 1
                if next_dist < visited[(next_row, next_col)]:
                    visited[(next_row, next_col)] = next_dist
                    stack.append((next_row, next_col, next_dist))
        if visited[(hole[0], hole[1])] == float('inf'):
            return -1
        else:
            return visited[(hole[0], hole[1])]