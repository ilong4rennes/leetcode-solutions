# Last updated: 10/4/2025, 8:53:41 PM
class Solution:
    class State:
        def __init__(self, row, col, effort):
            self.row = row
            self.col = col
            self.effort = effort
        
        def __lt__(self, other):
            return self.effort < other.effort
    
    def dijkstra(self, heights, row, col):
        rows, cols = len(heights), len(heights[0])
        n = rows * cols
        effortTo = [[-1] * cols for _ in range(rows)]
        pq = []
        heapq.heappush(pq, self.State(row, col, 0))
        while pq:
            state = heapq.heappop(pq)
            curRow, curCol = state.row, state.col
            curEffort = state.effort
            
            if effortTo[curRow][curCol] != -1: continue
            effortTo[curRow][curCol] = curEffort

            if curRow == rows - 1 and curCol == cols - 1:
                return curEffort

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                newRow, newCol = curRow + dr, curCol + dc
                if 0 <= newRow < rows and 0 <= newCol < cols:
                    effort = abs(heights[newRow][newCol] - heights[curRow][curCol])
                    newEffort = max(curEffort, effort)
                    if effortTo[newRow][newCol] != -1: continue
                    heapq.heappush(pq, self.State(newRow, newCol, newEffort))
        return -1

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        return self.dijkstra(heights, 0, 0)