# Last updated: 4/19/2025, 2:25:03 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = self.tree2graph(root)  # target is not used in tree2graph
        visited = {node: False for node in graph}
        queue = deque()
        queue.append(target)
        visited[target] = True
        steps = 0
        results = []

        while queue:
            if steps == k:
                return [node.val for node in queue]
            for _ in range(len(queue)):
                current = queue.popleft()
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            steps += 1
        return results
    
    def tree2graph(self, root):
        graph = defaultdict(list)
        self.inorder_recursive(root, graph)
        return graph
    
    def inorder_recursive(self, root, graph):
        if not root:
            return
        self.inorder_recursive(root.left, graph)
        if root.left:
            graph[root].append(root.left)
            graph[root.left].append(root)
        if root.right:
            graph[root].append(root.right)
            graph[root.right].append(root)
        self.inorder_recursive(root.right, graph)