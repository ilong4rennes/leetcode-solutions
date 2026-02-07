# Last updated: 2/7/2026, 5:08:08 PM
1class Solution:
2    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
3        n = len(matrix)
4        heap = []
5        heapq.heapify(heap)
6        step = 0
7        for i in range(min(n, k)):
8            heapq.heappush(heap, (matrix[i][0], i, 0))
9        while step < k:
10            num, row, col = heapq.heappop(heap)
11            if col + 1 < n:
12                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
13            step += 1
14        return num