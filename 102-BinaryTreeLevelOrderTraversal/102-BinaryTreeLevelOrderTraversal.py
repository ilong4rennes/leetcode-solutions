# Last updated: 1/28/2026, 3:12:06 PM
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
12        
13        while q:
14            size = len(q)
15            currLevel = []
16            for i in range(size):
17                curr = q.popleft()
18                currLevel.append(curr.val)
19                if curr.left:
20                    q.append(curr.left)
21                if curr.right:
22                    q.append(curr.right)
23            result.append(currLevel)
24        
25        return result
26                