class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        dist = {}
        for row in range(rows):
            for col in range(cols):
                dist[(row, col)] = float('inf')
        stack = deque()
        stack.append((start[0], start[1], 0))
        dist[tuple(start)] = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while stack:
            curr_row, curr_col, distance = stack.pop()
            for dr, dc in directions:
                next_row, next_col, new_dist = curr_row, curr_col, distance
                while (0 <= next_row + dr < rows and 
                       0 <= next_col + dc < cols and 
                       maze[next_row + dr][next_col + dc] == 0):
                    new_dist += 1
                    next_row += dr
                    next_col += dc
                if new_dist < dist[(next_row, next_col)]:
                    dist[(next_row, next_col)] = new_dist
                    stack.append((next_row, next_col, new_dist))

        return dist[tuple(destination)] if dist[tuple(destination)] != float('inf') else -1
        