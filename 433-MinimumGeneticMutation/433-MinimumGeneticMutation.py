# Last updated: 2/2/2026, 3:04:08 PM
1class Solution:
2    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
3        bank = set(bank)
4        # if endGene not in bank:
5        #     return -1
6
7        q = deque([startGene])
8        visited = set()
9        visited.add(startGene)
10        step = 0
11        while q:
12            size = len(q)
13            for _ in range(size):
14                currGene = q.popleft()
15                if currGene == endGene:
16                    return step
17                for to in self.getNeighbors(currGene):
18                    if to in bank and to not in visited:
19                        q.append(to)
20                        visited.add(to)
21            step += 1
22        return -1
23    
24    def getNeighbors(self, gene):
25        geneList = list(gene)
26        chars = ['A', 'C', 'G', 'T']
27        results = []
28        for i in range(len(geneList)):
29            for char in chars:
30                if geneList[i] == char: continue
31                else:
32                    newGeneList = geneList.copy()
33                    newGeneList[i] = char
34                    results.append(''.join(newGeneList))
35        return results
36
37