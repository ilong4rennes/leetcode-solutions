# Last updated: 10/7/2025, 1:47:44 PM
class Solution:
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
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def count(self):
            return self._count

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = self.UF(n)
        for edge in edges:
            node1, node2 = edge
            if uf.connected(node1, node2):
                return False
            else: 
                uf.union(node1, node2)
        return True if uf.count() == 1 else False


        