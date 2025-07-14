# Last updated: 7/14/2025, 12:49:24 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        self.result = 0
        self.traverse(root)
        return self.result
        
    def traverse(self, node):
        if node == None:
            return
        self.depth += 1
        if node.left == None and node.right == None:
            self.result = max(self.result, self.depth)
        self.traverse(node.left)
        self.traverse(node.right)
        self.depth -= 1
