# Last updated: 2/2/2026, 3:57:38 PM
1class Solution:
2    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
3        n = len(grid)
4        if grid[0][0] == 1 or grid[n-1][n-1] == 1: return -1
5        start = (0, 0)
6        q = deque([start])
7        grid[0][0] = 1
8        step = 1
9        while q:
10            size = len(q)
11            for _ in range(size):
12                currRow, currCol = q.popleft()
13                if currRow == n - 1 and currCol == n - 1:
14                    return step
15                for toRow, toCol in self.getNeighbors(currRow, currCol, n):
16                    if grid[toRow][toCol] != 1 and grid[toRow][toCol] == 0:
17                        q.append((toRow, toCol))
18                        grid[toRow][toCol] = 1
19            step += 1
20        return -1
21    
22    def getNeighbors(self, row, col, n):
23        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
24        results = []
25        for dr, dc in directions:
26            newR, newC = row + dr, col + dc
27            if 0 <= newR < n and 0 <= newC < n:
28                results.append((newR, newC))
29        return results