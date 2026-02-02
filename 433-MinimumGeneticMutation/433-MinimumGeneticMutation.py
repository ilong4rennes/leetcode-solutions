# Last updated: 2/2/2026, 3:03:15 PM
1class Solution:
2    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
3        q = deque([startGene])
4        visited = set()
5        visited.add(startGene)
6        bank = set(bank)
7        step = 0
8        while q:
9            size = len(q)
10            for _ in range(size):
11                currGene = q.popleft()
12                if currGene == endGene:
13                    return step
14                for to in self.getNeighbors(currGene):
15                    print(self.getNeighbors(currGene))
16                    if to in bank and to not in visited:
17                        q.append(to)
18                        visited.add(to)
19            step += 1
20        return -1
21    
22    def getNeighbors(self, gene):
23        geneList = list(gene)
24        chars = ['A', 'C', 'G', 'T']
25        results = []
26        for i in range(len(geneList)):
27            for char in chars:
28                if geneList[i] == char: continue
29                else:
30                    newGeneList = geneList.copy()
31                    newGeneList[i] = char
32                    results.append(''.join(newGeneList))
33        return results
34
35