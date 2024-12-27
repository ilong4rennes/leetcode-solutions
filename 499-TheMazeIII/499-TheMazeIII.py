class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        rows, cols = len(maze), len(maze[0])
        visited = {}
        path = {}
        for row in range(rows):
            for col in range(cols):
                visited[(row, col)] = float('inf')
                path[(row, col)] = ""
        visited[tuple(ball)] = 0
        stack = deque()
        stack.append((ball[0], ball[1], 0 ,""))
        directions = [(-1, 0, 'u'), (1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r')]

        
        while stack:
            curr_row, curr_col, dist, curr_path = stack.pop()
            for dr, dc, d in directions:
                next_row, next_col, next_dist, temp_path = curr_row, curr_col, dist, curr_path
                while (0 <= next_row + dr < rows and
                       0 <= next_col + dc < cols and
                       maze[next_row + dr][next_col + dc] == 0):
                       next_row += dr
                       next_col += dc
                       next_dist += 1
                       if [next_row, next_col] == hole: break
                if (next_dist < visited[(next_row, next_col)] or
                   (next_dist == visited[(next_row, next_col)] and 
                    temp_path < path[(next_row, next_col)])):
                        visited[(next_row, next_col)] = next_dist
                        path[(next_row, next_col)] = temp_path + d
                        stack.append((next_row, next_col, next_dist, temp_path + d))
        
        if visited[(hole[0], hole[1])] == float('inf'):
            return "impossible"
        else:
            return path[(hole[0], hole[1])]
