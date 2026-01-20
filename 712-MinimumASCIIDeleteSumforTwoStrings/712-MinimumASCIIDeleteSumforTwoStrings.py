# Last updated: 1/20/2026, 1:58:26 AM
1class Solution:
2    def minimumDeleteSum(self, s1: str, s2: str) -> int:
3        self.memo = [[-174] * (len(s2) + 1) for _ in range(len(s1) + 1)]
4        return self.dp(s1, 0, s2, 0)
5    
6    def dp(self, s1, id1, s2, id2):
7        res = 0
8        if id1 >= len(s1):
9            for i in range(id2, len(s2)):
10                res += ord(s2[i])
11            return res
12        if id2 >= len(s2):
13            for i in range(id1, len(s1)):
14                res += ord(s1[i])
15            return res
16        if self.memo[id1][id2] != -174:
17            return self.memo[id1][id2]
18        if s1[id1] == s2[id2]:
19            self.memo[id1][id2] = self.dp(s1, id1 + 1, s2, id2 + 1)
20        else:
21            self.memo[id1][id2] = min(self.dp(s1, id1 + 1, s2, id2) + ord(s1[id1]), 
22                                      self.dp(s1, id1, s2, id2 + 1) + ord(s2[id2]))
23        return self.memo[id1][id2]