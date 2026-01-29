# Last updated: 1/29/2026, 4:47:59 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9        q = deque([(1, root)])
10        maxWidth = 0
11        step = 0
12        while q:
13            size = len(q)
14            for i in range(size):
15                idx, currNode = q.popleft()
16                if currNode.left:
17                    num = idx * 2
18                    q.append((num, currNode.left))
19                if currNode.right:
20                    num = idx * 2 + 1
21                    q.append((num, currNode.right))
22                if i == 0:
23                    start = idx
24                if i == size - 1:
25                    end = idx
26                    width = end - start + 1
27            maxWidth = max(width, maxWidth)        
28        return maxWidth