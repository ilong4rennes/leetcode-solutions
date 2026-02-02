# Last updated: 2/2/2026, 3:57:25 PM
1class Solution:
2    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
3        n = len(grid)
4        if grid[0][0] == 1 or grid[n-1][n-1] == 1: return -1
5        def index(row, col): return row * n + col
6        start = (0, 0)
7        q = deque([start])
8        grid[0][0] = 1
9        step = 1
10        while q:
11            size = len(q)
12            for _ in range(size):
13                currRow, currCol = q.popleft()
14                if currRow == n - 1 and currCol == n - 1:
15                    return step
16                for toRow, toCol in self.getNeighbors(currRow, currCol, n):
17                    if grid[toRow][toCol] != 1 and grid[toRow][toCol] == 0:
18                        q.append((toRow, toCol))
19                        grid[toRow][toCol] = 1
20            step += 1
21        return -1
22    
23    def getNeighbors(self, row, col, n):
24        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
25        results = []
26        for dr, dc in directions:
27            newR, newC = row + dr, col + dc
28            if 0 <= newR < n and 0 <= newC < n:
29                results.append((newR, newC))
30        return results