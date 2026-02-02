# Last updated: 2/2/2026, 3:55:47 PM
1class Solution:
2    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
3        n = len(grid)
4        if grid[0][0] == 1 or grid[n-1][n-1] == 1: return -1
5        def index(row, col): return row * n + col
6        start = (0, 0)
7        q = deque([start])
8        visited = set()
9        visited.add(index(0, 0))
10        step = 1
11        while q:
12            size = len(q)
13            for _ in range(size):
14                currRow, currCol = q.popleft()
15                if currRow == n - 1 and currCol == n - 1:
16                    return step
17                for toRow, toCol in self.getNeighbors(currRow, currCol, n):
18                    idx = index(toRow, toCol)
19                    if idx not in visited and grid[toRow][toCol] == 0:
20                        q.append((toRow, toCol))
21                        visited.add(idx)
22            step += 1
23        return -1
24    
25    def getNeighbors(self, row, col, n):
26        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
27        results = []
28        for dr, dc in directions:
29            newR, newC = row + dr, col + dc
30            if 0 <= newR < n and 0 <= newC < n:
31                results.append((newR, newC))
32        return results