# Last updated: 9/24/2025, 8:02:51 PM
class UF:
    def __init__(self, n):
        self._count = n
        self.parent = [i for i in range(n)]
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ: return
        self.parent[rootQ] = rootP
        self._count -= 1
    
    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ
    
    def find(self, x):
        if self.parent[x] == x: return x
        root = self.find(self.parent[x])
        self.parent[x] = root
        return self.parent[x]
    
    def count(self):
        return self._count

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for e in edges:
            uf.union(e[0], e[1])
        return uf.count()