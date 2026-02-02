# Last updated: 2/2/2026, 3:03:41 PM
1class Solution:
2    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
3        bank = set(bank)
4        if endGene not in bank:
5            return -1
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
18                    print(self.getNeighbors(currGene))
19                    if to in bank and to not in visited:
20                        q.append(to)
21                        visited.add(to)
22            step += 1
23        return -1
24    
25    def getNeighbors(self, gene):
26        geneList = list(gene)
27        chars = ['A', 'C', 'G', 'T']
28        results = []
29        for i in range(len(geneList)):
30            for char in chars:
31                if geneList[i] == char: continue
32                else:
33                    newGeneList = geneList.copy()
34                    newGeneList[i] = char
35                    results.append(''.join(newGeneList))
36        return results
37
38