# Last updated: 2/4/2026, 7:19:04 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
9        if not root: return False
10        q = deque([root])
11        end = False
12        while q:
13            size = len(q)
14            for _ in range(size):
15                curr = q.popleft()
16                if curr == None: end = True
17                else:
18                    if end: return False
19                    q.append(curr.left)
20                    q.append(curr.right)
21        return True