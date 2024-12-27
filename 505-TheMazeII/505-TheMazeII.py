class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        # visited = {}
        dist = {}
        for row in range(rows):
            for col in range(cols):
                # visited[(row, col)] = False
                dist[(row, col)] = float('inf')
        stack = deque()
        stack.append(tuple(start))
        dist[tuple(start)] = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while stack:
            curr_row, curr_col = stack.pop()
            # if curr_row == destination[0] and curr_col == destination[1]:
            #     return dist[(curr_row, curr_col)]
            for dr, dc in directions:
                next_row, next_col = curr_row, curr_col
                steps = 0
                while (0 <= next_row + dr < rows and 
                       0 <= next_col + dc < cols and 
                       maze[next_row + dr][next_col + dc] == 0):
                    steps += 1
                    next_row += dr
                    next_col += dc
                # dist[(next_row, next_col)] = min(dist[(curr_row, curr_col)] + steps, dist[(next_row, next_col)])
    #             if visited[(next_row, next_col)] == False:
    #                 stack.append((next_row, next_col))
    #                 visited[(next_row, next_col)] = True
    #     return -1
        

                if dist[(curr_row, curr_col)] + steps < dist[(next_row, next_col)]:
                    dist[(next_row, next_col)] = dist[(curr_row, curr_col)] + steps
                    stack.append((next_row, next_col))
        
        # Return the shortest distance to the destination
        return dist[tuple(destination)] if dist[tuple(destination)] != float('inf') else -1
        