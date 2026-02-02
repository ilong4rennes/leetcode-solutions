# Last updated: 2/2/2026, 3:27:38 PM
1class Solution:
2    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
3        rows, cols = len(maze), len(maze[0])
4        def index(row, col):
5            return row * rows + col
6        er, ec = entrance
7        q = deque([entrance])
8        visited = set()
9        visited.add(index(er, ec))
10        step = 0
11        while q:
12            size = len(q)
13            for i in range(size):
14                currRow, currCol = q.popleft()
15                if self.isExit(currRow, currCol, maze) and (currRow != er or currCol != ec):
16                    return step
17                for toRow, toCol in self.getNeighbors(currRow, currCol, maze):
18                    idx = index(toRow, toCol)
19                    if idx not in visited:
20                        q.append((toRow, toCol))
21                        visited.add(idx)
22            step += 1
23        return -1
24
25    def isExit(self, row, col, maze):
26        rows, cols = len(maze), len(maze[0])
27        if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
28            return True
29        return False
30    
31    def getNeighbors(self, row, col, maze):
32        rows, cols = len(maze), len(maze[0])
33        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
34        results = []
35        for dr, dc in directions:
36            newRow, newCol = row + dr, col + dc
37            if 0 <= newRow < rows and 0 <= newCol < cols:
38                if maze[newRow][newCol] == '.':
39                    results.append((newRow, newCol))
40        return results