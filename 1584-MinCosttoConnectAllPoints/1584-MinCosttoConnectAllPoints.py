# Last updated: 10/8/2025, 4:11:30 AM
class Solution:
    class UF:
        def __init__(self, n):
            self._count = n
            self.parent = [i for i in range(n)]
        
        def union(self, p, q):
            rootP = self.find(p)
            rootQ = self.find(q)
            if rootP != rootQ:
                self.parent[rootQ] = rootP
            self._count -= 1
            return
        
        def connected(self, p, q):
            return self.find(p) == self.find(q)
        
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
        def count(self):
            return self._count

    def md(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = self.UF(n)
        graph = []
        for id1 in range(n):
            for id2 in range(id1 + 1, n):
                x1, y1 = points[id1]
                x2, y2 = points[id2]
                cost = self.md(x1, y1, x2, y2)
                graph.append((id1, id2, cost))
        graph.sort(key=lambda x:x[2])
        mst = 0
        # numNode = 1 
        for _from, _to, cost in graph:
            # if numNode == n:
            #     return mst
            if uf.connected(_from, _to):
                continue
            else:
                uf.union(_from, _to)
                mst += cost
                # numNode += 1
        return mst
        