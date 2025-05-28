# Last updated: 5/28/2025, 8:51:34 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root:
            self.traverse(root.left, root.right)
        return root
    
    def traverse(self, left, right):
        if left is None or right is None: return
        left.next = right
        self.traverse(left.left, left.right)
        self.traverse(right.left, right.right)
        self.traverse(left.right, right.left)