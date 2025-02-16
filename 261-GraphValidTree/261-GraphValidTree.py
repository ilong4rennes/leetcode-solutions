class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1 and not edges: return True
        if not edges: return False

        adj_list = self.transform_graph(n, edges)
        start = edges[0][0]
        visited = set()
        visited.add(start)
        stack = deque()
        stack.append((start, -1))
        while stack:
            currNode, parent = stack.pop()
            for neighbor in adj_list[currNode]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append((neighbor, currNode))
                elif neighbor != parent: 
                    return False
        return True if len(visited) == n else False
    
    def transform_graph(self, n, edges):
        adj_list = defaultdict(list)
        for start, end in edges:
            adj_list[start].append(end)
            adj_list[end].append(start)
        return adj_list