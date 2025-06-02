# Last updated: 6/2/2025, 3:53:40 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.val2ind = dict()

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        for i in range(len(inorder)):
            self.val2ind[inorder[i]] = i
        return self.build(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)
    
    def build(self, inorder, inStart, inEnd, postorder, postStart, postEnd):
        if inStart > inEnd or postStart > postEnd: return 
        rootVal = postorder[postEnd]
        root = TreeNode(rootVal)
        rootId = self.val2ind[rootVal]
        leftLen = rootId - inStart
        root.left = self.build(inorder, inStart, inStart + leftLen - 1,
                               postorder, postStart, postStart + leftLen - 1)
        root.right = self.build(inorder, rootId + 1, inEnd, 
                                postorder, postStart + leftLen, postEnd - 1)
        return root