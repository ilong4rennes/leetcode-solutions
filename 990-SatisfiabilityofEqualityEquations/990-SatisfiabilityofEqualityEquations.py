# Last updated: 9/24/2025, 10:57:18 PM
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
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UF(26)
        for eq in equations:
            l1, l2, relation = eq[0], eq[3], eq[1:3]
            if relation == "==":
                uf.union(ord(l1) - ord("a"), ord(l2) - ord("a"))
        for eq in equations:
            l1, l2, relation = eq[0], eq[3], eq[1:3]
            if relation == "!=":
                if uf.connected(ord(l1) - ord("a"), ord(l2) - ord("a")):
                    return False
        return True