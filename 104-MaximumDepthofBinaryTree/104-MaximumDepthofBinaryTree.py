# Last updated: 5/26/2025, 11:38:52 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 1
        self.result = 0
        self.traverse(depth, root, self.result)
        return self.result 
    
    def traverse(self, depth, root, result):
        if root is None: return
        if root.left is None and root.right is None:
            self.result = max(depth, self.result)
        depth += 1
        self.traverse(depth, root.left, self.result)
        self.traverse(depth, root.right, self.result)
        depth -= 1