# Last updated: 1/20/2026, 12:54:17 AM
1class Solution:
2    def minDistance(self, word1: str, word2: str) -> int:
3        return len(word1) + len(word2) - 2 * self.LCS(word1, word2)
4    
5    def LCS(self, word1, word2):
6        self.memo = [[-174] * (len(word2) + 1) for _ in range(len(word1) + 1)]
7        return self.dp(word1, 0, word2, 0)
8
9    def dp(self, word1, id1, word2, id2):
10        if id1 >= len(word1) or id2 >= len(word2):
11            return 0
12        if self.memo[id1][id2] != -174:
13            return self.memo[id1][id2]
14        if word1[id1] == word2[id2]:
15            self.memo[id1][id2] = self.dp(word1, id1 + 1, word2, id2 + 1) + 1
16        else: 
17            self.memo[id1][id2] = max(self.dp(word1, id1, word2, id2 + 1),
18                                      self.dp(word1, id1 + 1, word2, id2))
19        return self.memo[id1][id2]