# Last updated: 2/5/2026, 11:26:47 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def minDepth(self, root: Optional[TreeNode]) -> int:
9        if not root: return 0
10        q = deque([root])
11        minDepth = float('inf')
12        depth = 1
13        while q:
14            size = len(q)
15            for _ in range(size):
16                curr = q.popleft()
17                if not curr.left and not curr.right:
18                    minDepth = min(minDepth, depth)
19                if curr.left:
20                    q.append(curr.left)
21                if curr.right:
22                    q.append(curr.right)
23            depth += 1
24        return minDepth