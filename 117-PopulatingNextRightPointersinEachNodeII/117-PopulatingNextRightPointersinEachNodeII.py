# Last updated: 2/4/2026, 8:41:20 AM
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
16        while q:
17            size = len(q)
18            pre = None 
19            for _ in range(size):
20                curr = q.popleft()
21                if pre:
22                    pre.next = curr
23                pre = curr
24                if curr.left:
25                    q.append(curr.left)
26                if curr.right:
27                    q.append(curr.right)
28        return dummy