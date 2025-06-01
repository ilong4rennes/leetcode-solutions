# Last updated: 6/1/2025, 5:47:56 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.val2ind = {}

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        for i, v in enumerate(inorder):
            self.val2ind[v] = i
        root = self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
        return root
    
    def build(self, preorder, preStart, preEnd, inorder, inStart, inEnd):
        if preStart > preEnd or inStart > inEnd:
            return None
        rootVal = preorder[preStart]
        root = TreeNode(rootVal)
        rootId = self.val2ind[rootVal]
        leftLen = rootId - inStart
        
        root.left = self.build(preorder, preStart + 1, preStart + leftLen, 
                               inorder, inStart, inStart + leftLen - 1)
        root.right = self.build(preorder, preStart + leftLen + 1, preEnd, 
                                inorder, rootId + 1, inEnd)
        return root