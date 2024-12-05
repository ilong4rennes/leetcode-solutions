class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        def dfs(maze, start):
            rows, cols = len(maze), len(maze[0])
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
            visited = [[math.inf for _ in range(cols)] for _ in range(rows)]
            visited[start[0]][start[1]] = 0  # Distance to start is 0
            stack = deque([(start[0], start[1], 0)])  # (row, col, distance)

            while stack:
                x, y, dist = stack.pop()
                
                for dx, dy in directions:
                    nx, ny, d = x, y, dist
                    # Roll the ball until it hits a wall
                    while 0 <= nx + dx < rows and 0 <= ny + dy < cols and maze[nx + dx][ny + dy] == 0:
                        nx += dx
                        ny += dy
                        d += 1
                    
                    if d < visited[nx][ny]:  # Only visit if we find a shorter distance
                        visited[nx][ny] = d
                        stack.append((nx, ny, d))

            return visited

        visited = dfs(maze, start)
        dest_distance = visited[destination[0]][destination[1]]
        return dest_distance if dest_distance != math.inf else -1