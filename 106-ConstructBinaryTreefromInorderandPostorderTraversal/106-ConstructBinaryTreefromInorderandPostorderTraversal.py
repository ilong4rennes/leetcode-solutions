# Last updated: 6/2/2025, 5:53:01 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.val2ind = {}

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        for i in range(len(postorder)):
            self.val2ind[postorder[i]] = i
        return self.build(preorder, 0, len(preorder) - 1, postorder, 0, len(postorder) - 1)
    
    def build(self, preorder, preStart, preEnd, postorder, postStart, postEnd):
        if preStart > preEnd or postStart > postEnd: return
        if preStart == preEnd:
            return TreeNode(preorder[preStart])
        rootVal = preorder[preStart]
        root = TreeNode(rootVal)
        leftroot = preorder[preStart + 1]
        lrIndex = self.val2ind[leftroot]
        leftLen = lrIndex - postStart + 1
        root.left = self.build(preorder, preStart + 1, preStart + leftLen,
                               postorder, postStart, lrIndex)
        root.right = self.build(preorder, preStart + leftLen + 1, preEnd, 
                                postorder, lrIndex + 1, postEnd - 1)
        return root