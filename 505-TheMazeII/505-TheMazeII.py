class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        visited = self.dfs(maze, start)
        distance = visited[destination[0]][destination[1]]
        return distance if distance != math.inf else -1
    
    def dfs(self, maze, start):
        rows, cols = len(maze), len(maze[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[math.inf for col in range(cols)] for row in range(rows)]
        stack = deque()
        stack.append((start[0], start[1], 0))
        visited[start[0]][start[1]] = 0
        while stack:
            x, y, dist = stack.pop()
            for (dx, dy) in directions:
                nx, ny, d = x, y, dist
                while ((0 <= nx + dx < rows) and (0 <= ny + dy < cols) 
                  and (maze[nx + dx][ny + dy] == 0)):
                    nx += dx
                    ny += dy
                    d += 1
                if d < visited[nx][ny]:
                    visited[nx][ny] = d
                    stack.append((nx, ny, d))
        return visited