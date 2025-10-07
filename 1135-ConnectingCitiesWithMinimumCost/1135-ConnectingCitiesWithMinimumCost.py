# Last updated: 10/7/2025, 2:23:44 PM
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

    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        uf = self.UF(n + 1)
        connections.sort(key=lambda x:x[2])
        mst = 0
        for connection in connections:
            x, y, cost = connection
            if uf.connected(x, y):
                continue
            else:
                uf.union(x, y)
                mst += cost
        return mst if uf.count() == 2 else -1