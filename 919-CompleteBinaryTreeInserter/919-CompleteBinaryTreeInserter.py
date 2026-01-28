# Last updated: 1/28/2026, 3:42:44 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class CBTInserter:
8
9    def __init__(self, root: Optional[TreeNode]):
10        self.root = root
11        self.q = deque([root])
12        self.parents = deque()
13        while self.q:
14            size = len(self.q)
15            for i in range(size):
16                curr = self.q.popleft()
17                if curr.left is None or curr.right is None:
18                    self.parents.append(curr)
19                if curr.left:
20                    self.q.append(curr.left)
21                if curr.right:
22                    self.q.append(curr.right)
23
24
25    def insert(self, val: int) -> int:
26        parent = self.parents[0]
27        newNode = TreeNode(val)
28        if parent.left is None:
29            parent.left = newNode
30        else:
31            parent.right = newNode
32            self.parents.popleft()
33        self.parents.append(newNode)
34        return parent.val
35        
36
37    def get_root(self) -> Optional[TreeNode]:
38        return self.root
39        
40
41
42# Your CBTInserter object will be instantiated and called as such:
43# obj = CBTInserter(root)
44# param_1 = obj.insert(val)
45# param_2 = obj.get_root()