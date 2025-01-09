# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        self.memo = {}
        return max(self.DFS(root, True, 0),
                   self.DFS(root, False, 0))
        
    def DFS(self, root, robbed, maxMoney):
        if root == None: return maxMoney
        if (root, robbed) in self.memo:
            return self.memo[(root, robbed)]
        if robbed: 
            maxMoney += root.val
            left = self.DFS(root.left, False, 0)
            right = self.DFS(root.right, False, 0)
        else:
            left = max(self.DFS(root.left, True, 0), 
                       self.DFS(root.left, False, 0))
            right = max(self.DFS(root.right, True, 0), 
                        self.DFS(root.right, False, 0))
        self.memo[(root, robbed)] = maxMoney + left + right
        return self.memo[(root, robbed)]