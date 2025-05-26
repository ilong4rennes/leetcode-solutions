# Last updated: 5/27/2025, 2:20:01 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.traverse(root)
        return self.result
    
    def traverse(self, node):
        if not node: return 0
        leftDepth = self.traverse(node.left)
        rightDepth = self.traverse(node.right)
        maxDepth = max(leftDepth, rightDepth)
        maxDiameter = leftDepth + rightDepth
        self.result = max(self.result, maxDiameter)
        return maxDepth + 1