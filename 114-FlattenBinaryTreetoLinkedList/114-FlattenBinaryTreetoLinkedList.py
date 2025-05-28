# Last updated: 5/28/2025, 9:47:02 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        self.flatten(root.left)
        self.flatten(root.right)
        print(root.val)
        left = root.left
        right = root.right
        root.left = None
        root.right = left
        p = root
        while p.right:  
            p = p.right
        p.right = right