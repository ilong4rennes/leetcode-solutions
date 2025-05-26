# Last updated: 5/27/2025, 12:15:16 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        self.traverse(root)
        return self.result
    
    def traverse(self, node):
        if not node: return
        self.result.append(node.val)
        self.traverse(node.left)
        self.traverse(node.right)