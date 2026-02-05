# Last updated: 2/5/2026, 11:09:13 AM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
5        self.val = val
6        self.children = children
7"""
8
9class Solution:
10    def levelOrder(self, root: 'Node') -> List[List[int]]:
11        if not root: return []
12        q = deque([root])
13        result = []
14        while q:
15            size = len(q)
16            level = []
17            for _ in range(size):
18                curr = q.popleft()
19                level.append(curr.val)
20                for to in curr.children:
21                    q.append(to)
22            result.append(level)
23        return result