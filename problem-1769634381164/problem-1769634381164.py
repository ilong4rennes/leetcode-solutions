# Last updated: 1/28/2026, 4:06:21 PM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
5        self.val = val
6        self.left = left
7        self.right = right
8        self.next = next
9"""
10
11class Solution:
12    def connect(self, root: 'Node') -> 'Node':
13        if not root: return root
14        dummy = root
15        q = deque([root])
16
17        while q:
18            size = len(q)
19            pre = None
20            for _ in range(size):
21                curr = q.popleft()
22                if pre:
23                    pre.next = curr
24                pre = curr
25                if curr.left:
26                    q.append(curr.left)
27                if curr.right:
28                    q.append(curr.right)
29        return dummy