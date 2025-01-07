class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        # build the graph
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        # use bfs to find one end of the longest path
        node_a, dist = self.bfs(graph, 0)
        # pass one end into bfs again to find the diameter
        node_b, diameter = self.bfs(graph, node_a)
        return diameter
        
    def bfs(self, graph, start):
        queue = deque([(start, 0)])
        visited = set()
        visited.add(start)
        maxDist = 0
        while queue:
            node, dist = queue.popleft()
            maxDist = max(dist, maxDist)
            length = len(graph[node])
            index = 0
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, dist + 1))
                    visited.add(neighbor)
                else: 
                    index += 1
            if index == length and not queue:
                return node, maxDist
