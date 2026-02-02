# Last updated: 2/2/2026, 3:02:21 PM
1class Solution:
2    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
3        q = deque([startGene])
4        visited = set()
5        visited.add(startGene)
6        step = 0
7        while q:
8            size = len(q)
9            for _ in range(size):
10                currGene = q.popleft()
11                if currGene == endGene:
12                    return step
13                for to in self.getNeighbors(currGene):
14                    print(self.getNeighbors(currGene))
15                    if to in bank and to not in visited:
16                        q.append(to)
17                        visited.add(to)
18            step += 1
19        return -1
20    
21    def getNeighbors(self, gene):
22        geneList = list(gene)
23        chars = ['A', 'C', 'G', 'T']
24        results = []
25        for i in range(len(geneList)):
26            for char in chars:
27                if geneList[i] == char: continue
28                else:
29                    newGeneList = geneList.copy()
30                    newGeneList[i] = char
31                    results.append(''.join(newGeneList))
32        return results
33
34