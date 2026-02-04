# Last updated: 2/4/2026, 5:40:58 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
9        if not root: return []
10        q = deque([root])
11        result = []
12        while q:
13            size = len(q)
14            levelSum = 0
15            for _ in range(size):
16                curr = q.popleft()
17                levelSum += curr.val
18                if curr.left:
19                    q.append(curr.left)
20                if curr.right:
21                    q.append(curr.right)
22            result.append(levelSum / size)
23        return result