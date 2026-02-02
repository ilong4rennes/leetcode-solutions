# Last updated: 2/2/2026, 2:14:17 PM
1class Solution:
2    def canReach(self, arr: List[int], start: int) -> bool:
3        n = len(arr)
4        q = deque([start])
5        visited = set()
6        visited.add(start)
7        while q:
8            size = len(q)
9            for _ in range(size):
10                curr = q.popleft()
11                if arr[curr] == 0:
12                    return True
13                leftIndex = curr - arr[curr]
14                rightIndex = curr + arr[curr]
15                if leftIndex not in visited and 0 <= leftIndex < n:
16                    q.append(leftIndex)
17                    visited.add(leftIndex)
18                if rightIndex not in visited and 0 <= rightIndex < n:
19                    q.append(rightIndex)
20                    visited.add(rightIndex)
21        return False