# Last updated: 5/26/2025, 11:58:57 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        self.result = 0
        self.traverse(depth, root)
        return self.result 
    
    def traverse(self, depth, root):
        if root is None: return
        depth += 1
        if root.left is None and root.right is None:
            self.result = max(depth, self.result)
        self.traverse(depth, root.left)
        self.traverse(depth, root.right)
        depth -= 1