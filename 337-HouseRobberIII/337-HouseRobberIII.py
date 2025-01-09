# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        self.memo = {}
        return max(self.DFS(root, True), self.DFS(root, False))
        
    def DFS(self, root, robbed):
        if not root: return 0
        if (root, robbed) in self.memo:
            return self.memo[(root, robbed)]
        if robbed:
            currVal = root.val
            left = self.DFS(root.left, False)
            right = self.DFS(root.right, False)
        else:
            currVal = 0
            left = max(self.DFS(root.left, True), 
                       self.DFS(root.left, False))
            right = max(self.DFS(root.right, True),
                        self.DFS(root.right, False))
        if (root, robbed) not in self.memo:
            self.memo[(root, robbed)] = currVal + left + right
        return currVal + left + right