# Last updated: 2/4/2026, 5:29:12 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
9        if not root: return True
10        q = deque([root])
11        isEvenLevel = True
12        while q:
13            size = len(q)
14            pre = None
15            for _ in range(size):
16                curr = q.popleft()
17                if isEvenLevel:
18                    if curr.val % 2 == 0: return False
19                    if pre:
20                        if pre.val >= curr.val: return False
21                if not isEvenLevel:
22                    if curr.val % 2 == 1: return False
23                    if pre:
24                        if pre.val <= curr.val: return False
25                pre = curr
26                if curr.left: 
27                    q.append(curr.left)
28                if curr.right:
29                    q.append(curr.right)
30            isEvenLevel = not isEvenLevel
31        return True