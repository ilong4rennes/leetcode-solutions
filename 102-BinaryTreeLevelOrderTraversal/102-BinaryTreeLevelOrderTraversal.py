# Last updated: 2/3/2026, 1:00:44 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        if not root: return []
10        q = deque([root])
11        result = []
12        while q:
13            stepLevel = []
14            size = len(q)
15            for _ in range(size):
16                curr = q.popleft()
17                stepLevel.append(curr.val)
18                if curr.left:
19                    q.append(curr.left)
20                if curr.right:
21                    q.append(curr.right)
22            result.append(stepLevel)
23        return result