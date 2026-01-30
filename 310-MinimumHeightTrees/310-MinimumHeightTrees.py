# Last updated: 1/30/2026, 4:09:59 AM
1class Solution:
2    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
3        graph = self.edges2graph(edges)
4        q = deque()
5        visited = set()
6        for i in range(n):
7            if len(graph[i]) == 1:
8                q.append(i)
9                visited.add(i)
10        while len(graph) > 2:
11            size = len(q)
12            for _ in range(size):
13                curr = q.popleft()
14                for to in graph[curr]:
15                    graph[to].remove(curr)
16                    if len(graph[to]) == 1:
17                        q.append(to)
18                        visited.add(to)
19                del graph[curr]
20        return list(graph.keys())
21    
22    def edges2graph(self, edges):
23        graph = defaultdict(list)
24        for node1, node2 in edges:
25            graph[node1].append(node2)
26            graph[node2].append(node1)
27        return graph