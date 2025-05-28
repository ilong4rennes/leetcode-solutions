# Last updated: 5/29/2025, 3:17:41 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None
        maxVal = max(nums)
        maxPos = nums.index(maxVal)
        root = TreeNode(maxVal)
        root.left = self.constructMaximumBinaryTree(nums[:maxPos])
        root.right = self.constructMaximumBinaryTree(nums[maxPos + 1:])
        return root