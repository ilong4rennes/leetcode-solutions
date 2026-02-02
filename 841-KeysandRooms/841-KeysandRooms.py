# Last updated: 2/2/2026, 1:51:25 PM
1class Solution:
2    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
3        n = len(rooms)
4        q = deque([0])
5        visited = set()
6        visited.add(0)
7        while q:
8            size = len(q)
9            for _ in range(size):
10                curr = q.popleft()
11                for to in rooms[curr]:
12                    if to not in visited:
13                        visited.add(to)
14                        q.append(to)
15        return True if len(visited) == n else False
16