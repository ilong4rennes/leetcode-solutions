class Solution:
    def findRedundantConnection(self, edges):
        def getCycleStartWithParents(adj_list):
            parents = [-1] * N
            visited = [False] * N
            stack = [0]
            while (stack):
                src = stack.pop()
                visited[src] = True
                for nxt in adj_list[src]:
                    if not visited[nxt]:
                        parents[nxt] = src
                        stack.append(nxt)
                    if visited[nxt] and nxt != parents[src]:
                        parents[nxt] = src
                        return nxt, parents
            return -1, parents

        N = len(edges)
        adj_list = [[] for _ in range(N)]
        for edge in edges:
            adj_list[edge[0] - 1].append(edge[1] - 1)
            adj_list[edge[1] - 1].append(edge[0] - 1)

        node, parents = getCycleStartWithParents(adj_list)
        node_copy = node

        node_cycle = set()
        while True:
            node_cycle.add(node)
            node = parents[node]
            if node == node_copy:
                break

        for i in range(len(edges) - 1, -1, -1):
            if (edges[i][0] - 1) in node_cycle and (edges[i][1] - 1) in node_cycle:
                return edges[i]

        return -1