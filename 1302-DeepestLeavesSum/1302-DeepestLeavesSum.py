# Last updated: 2/4/2026, 9:58:06 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
9        if not root: return 0
10        result = 0
11        q = deque([root])
12        while q:
13            size = len(q)
14            levelSum = 0
15            for _ in range(size):
16                curr = q.popleft()
17                levelSum += curr.val
18                if curr.left:
19                    q.append(curr.left)
20                if curr.right:
21                    q.append(curr.right)
22            result = levelSum
23        return result