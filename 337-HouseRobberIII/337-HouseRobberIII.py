# Last updated: 1/22/2026, 6:17:32 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rob(self, root: Optional[TreeNode]) -> int:
9        self.memo = {}
10        return self.dp(root)
11    
12    def dp(self, node):
13        if not node: return 0
14        if node in self.memo: return self.memo[node]
15        rob = (node.val +
16               (self.dp(node.left.left) if node.left and node.left.left else 0) +
17               (self.dp(node.left.right) if node.left and node.left.right else 0) +
18               (self.dp(node.right.left) if node.right and node.right.left else 0) +
19               (self.dp(node.right.right) if node.right and node.right.right else 0))
20        notRob = ((self.dp(node.left) if node.left else 0) + 
21                  (self.dp(node.right) if node.right else 0))
22        self.memo[node] = max(rob, notRob)
23        return self.memo[node]