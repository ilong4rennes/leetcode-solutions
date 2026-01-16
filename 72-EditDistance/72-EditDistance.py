# Last updated: 1/15/2026, 7:23:34 PM
1class Solution:
2    def minDistance(self, word1: str, word2: str) -> int:
3        id1, id2 = len(word1) - 1, len(word2) - 1
4        self.memo = [[-174] * len(word2) for _ in range(len(word1))]
5        return self.dp(id1, word1, id2, word2)
6    
7    def dp(self, id1, word1, id2, word2):
8        if id1 < 0: return id2 + 1
9        if id2 < 0: return id1 + 1
10        if self.memo[id1][id2] != -174: 
11            return self.memo[id1][id2]
12        
13        if word1[id1] == word2[id2]:
14            self.memo[id1][id2] =  self.dp(id1 - 1, word1, id2 - 1, word2)
15        else:
16            self.memo[id1][id2] = self.min3(
17                self.dp(id1, word1, id2 - 1, word2) + 1,
18                self.dp(id1 - 1, word1, id2, word2) + 1,
19                self.dp(id1 - 1, word1, id2 - 1, word2) + 1
20            )
21        return self.memo[id1][id2]
22
23    def min3(self, a, b, c):
24        return min(a, min(b, c))