# Last updated: 6/1/2025, 4:42:38 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = self.build(preorder, inorder)
        return root
    
    def build(self, preorder, inorder):
        if not preorder: return
        rootVal = preorder[0]
        root = TreeNode(rootVal)
        rootId = inorder.index(rootVal)
        inorderLeft, inorderRight = inorder[:rootId], inorder[rootId + 1:]
        leftLen, rightLen = len(inorderLeft), len(inorderRight)
        preorderLeft, preorderRight = preorder[1 : 1 + leftLen], preorder[1 + leftLen :]
        root.left = self.build(preorderLeft, inorderLeft)
        root.right = self.build(preorderRight, inorderRight)
        return root