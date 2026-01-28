# Last updated: 1/27/2026, 11:45:14 PM
1class Solution:
2    def openLock(self, deadends: List[str], target: str) -> int:
3        initial = '0000'
4        deadends = set(deadends)
5        if initial in deadends: return -1
6
7        visited = set()
8        visited.add(initial)
9        q = deque([initial])
10        step = 0
11
12        while q:
13            size = len(q)
14            for i in range(size):
15                curr = q.popleft()
16                if curr == target:
17                    return step
18                for to in self.getNeighbors(curr):
19                    if to not in visited and to not in deadends:
20                        visited.add(to)
21                        q.append(to)
22            step += 1
23        return -1
24    
25    def getNeighbors(self, lock):
26        neighbors = []
27        for idx in range(len(lock)):
28            neighbors.append(self.plusOne(lock, idx))
29            neighbors.append(self.minusOne(lock, idx))
30        return neighbors
31    
32    def plusOne(self, lock, idx):
33        lockList = list(lock)
34        if lock[idx] == '9':
35            lockList[idx] = '0'
36        else:
37            lockList[idx] = str(int(lock[idx]) + 1)
38        return ''.join(lockList)
39    
40    def minusOne(self, lock, idx):
41        lockList = list(lock)
42        if lock[idx] == '0':
43            lockList[idx] = '9'
44        else:
45            lockList[idx] = str(int(lock[idx]) - 1)
46        return ''.join(lockList)