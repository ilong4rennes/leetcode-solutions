# Last updated: 1/29/2026, 8:51:37 PM
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
16        while q:
17            if step == k:
18                return [node.val for node in q]
19            size = len(q)
20            for _ in range(size):
21                curr = q.popleft()
22                for to in self.graph[curr]:
23                    if to not in visited:
24                        q.append(to)
25                        visited.add(to)
26            step += 1
27        return []
28
29    def tree2graph(self, node, parent):
30        if parent:
31            self.graph[node].append(parent)
32            self.graph[parent].append(node)
33        if node.left:
34            self.tree2graph(node.left, node)
35        if node.right:
36            self.tree2graph(node.right, node)