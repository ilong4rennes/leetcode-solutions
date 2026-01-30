# Last updated: 1/30/2026, 4:10:22 AM
1class Solution:
2    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
3        graph = self.edges2graph(edges)
4        q = deque()
5        for i in range(n):
6            if len(graph[i]) == 1:
7                q.append(i)
8        while len(graph) > 2:
9            size = len(q)
10            for _ in range(size):
11                curr = q.popleft()
12                for to in graph[curr]:
13                    graph[to].remove(curr)
14                    if len(graph[to]) == 1:
15                        q.append(to)
16                del graph[curr]
17        return list(graph.keys())
18    
19    def edges2graph(self, edges):
20        graph = defaultdict(list)
21        for node1, node2 in edges:
22            graph[node1].append(node2)
23            graph[node2].append(node1)
24        return graph