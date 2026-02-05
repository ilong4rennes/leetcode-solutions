# Last updated: 2/5/2026, 11:18:58 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        if not root: return 0
10        q = deque([root])
11        maxDepth = 0
12        while q:
13            size = len(q)
14            for _ in range(size):
15                curr = q.popleft()
16                if curr.left:
17                    q.append(curr.left)
18                if curr.right:
19                    q.append(curr.right)
20            maxDepth += 1
21        return maxDepth