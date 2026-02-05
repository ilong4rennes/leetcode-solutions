# Last updated: 2/5/2026, 10:52:16 AM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
5        self.val = val
6        self.children = children
7"""
8
9class Solution:
10    def preorder(self, root: 'Node') -> List[int]:
11        if not root: return []
12        self.result = []
13        self.traverse(root)
14        return self.result
15    
16    def traverse(self, node):
17        self.result.append(node.val)
18        for to in node.children:
19            self.traverse(to)
20