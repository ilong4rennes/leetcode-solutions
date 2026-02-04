# Last updated: 2/4/2026, 8:28:20 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
9        if not root: return []
10        q = deque([root])
11        result = []
12        while q:
13            size = len(q)
14            maxNum = -float('inf')
15            for _ in range(size):
16                curr = q.popleft()
17                maxNum = max(curr.val, maxNum)
18                if curr.left:
19                    q.append(curr.left)
20                if curr.right:
21                    q.append(curr.right)
22            result.append(maxNum)
23        return result