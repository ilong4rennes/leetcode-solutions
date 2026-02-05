# Last updated: 2/4/2026, 9:29:00 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
9        if not root: return 0
10        q = deque([root])
11        maxSum, level, result = -float('inf'), 1, 1
12        while q:
13            size = len(q)
14            currSum = 0
15            for _ in range(size):
16                curr = q.popleft()
17                currSum += curr.val
18                if curr.left:
19                    q.append(curr.left)
20                if curr.right:
21                    q.append(curr.right)
22            if currSum > maxSum:
23                maxSum = currSum
24                result = level
25            level += 1
26        return result