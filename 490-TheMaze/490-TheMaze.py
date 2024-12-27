class Solution:
    def dfs(self, maze, visited, start, destination):
        m, n = len(maze), len(maze[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        stack = deque()
        stack.append(start)
        visited[tuple(start)] = True
        
        while stack:
            current = stack.pop()
            if current == destination:
                return True
            
            # Explore in all 4 directions
            for direction in directions:
                x, y = current
                # Roll the ball in the current direction until hitting a wall
                while 0 <= x + direction[0] < m and 0 <= y + direction[1] < n and maze[x + direction[0]][y + direction[1]] == 0:
                    x += direction[0]
                    y += direction[1]
                
                if not visited[(x, y)]:
                    stack.append([x, y])
                    visited[(x, y)] = True
                    
        return False

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        visited = {(i, j): False for i in range(m) for j in range(n)}
        return self.dfs(maze, visited, start, destination)
            