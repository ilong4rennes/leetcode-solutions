# Last updated: 1/27/2026, 7:46:06 PM
1class Solution:
2    def slidingPuzzle(self, board: List[List[int]]) -> int:
3        boardStr = ''
4        for i in range(len(board)):
5            for j in range(len(board[0])):
6                boardStr += str(board[i][j])
7        target = '123450'
8
9        visited = set()
10        visited.add(boardStr)
11        q = deque([boardStr])
12        step = 0
13        while q:
14            size = len(q)
15            for i in range(size):
16                curr = q.popleft()
17                if curr == target:
18                    return step
19                for nextPuzzle in self.getNeighbors(curr):
20                    if nextPuzzle not in visited:
21                        q.append(nextPuzzle)
22                        visited.add(nextPuzzle)
23            step += 1
24        return -1
25    
26    def getNeighbors(self, board):
27        transition = [
28            [1, 3],
29            [0, 2, 4],
30            [1, 5],
31            [0, 4],
32            [1, 3, 5],
33            [2, 4]
34        ]
35        emptyInd = board.index('0')
36        swap = transition[emptyInd]
37        neighbors = []
38        for pos in swap:
39            neighbors.append(self.swap(emptyInd, pos, board))
40        return neighbors
41    
42    def swap(self, id1, id2, board):
43        boardList = list(board)
44        boardList[id1], boardList[id2] = boardList[id2], boardList[id1]
45        return ''.join(boardList)
46