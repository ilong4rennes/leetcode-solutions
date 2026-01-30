# Last updated: 1/29/2026, 8:49:08 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
10        self.graph = defaultdict(list)
11        self.tree2graph(root, None)
12        q = deque([target])
13        visited = set()
14        visited.add(target)
15        step = 0
16        result = []
17        while q:
18            size = len(q)
19            for _ in range(size):
20                curr = q.popleft()
21                if step == k:
22                    result.append(curr.val)
23                for to in self.graph[curr]:
24                    if to not in visited:
25                        q.append(to)
26                        visited.add(to)
27            step += 1
28        return result
29
30    def tree2graph(self, node, parent):
31        if parent:
32            self.graph[node].append(parent)
33            self.graph[parent].append(node)
34        if node.left:
35            self.tree2graph(node.left, node)
36        if node.right:
37            self.tree2graph(node.right, node)