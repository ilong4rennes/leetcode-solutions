# Last updated: 2/4/2026, 8:12:18 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        if not root: return []
10        q = deque([root])
11        result = []
12        step = 0
13        while q:
14            size = len(q)
15            level = []
16            for _ in range(size):
17                curr = q.popleft()
18                level.append(curr.val)
19                if curr.left:
20                    q.append(curr.left)
21                if curr.right:
22                    q.append(curr.right)
23            if step % 2 == 1:
24                level = level[::-1]
25            result.append(level)
26            step += 1
27        return result