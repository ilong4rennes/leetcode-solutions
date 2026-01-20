# Last updated: 1/19/2026, 11:29:49 PM
1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        self.memo = [[-174] * (len(text2) + 1) for _ in range(len(text1) + 1)]
4        return self.dp(text1, 0, text2, 0)
5    
6    def dp(self, text1, id1, text2, id2):
7        if id1 >= len(text1) or id2 >= len(text2):
8            return 0
9        if self.memo[id1][id2] != -174:
10            return self.memo[id1][id2]
11        if text1[id1] == text2[id2]:
12            self.memo[id1][id2] = self.dp(text1, id1 + 1, text2, id2 + 1) + 1
13        else:
14            self.memo[id1][id2] = max(self.dp(text1, id1, text2, id2 + 1),
15                                      self.dp(text1, id1 + 1, text2, id2))
16        return self.memo[id1][id2]