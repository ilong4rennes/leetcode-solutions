# Last updated: 1/15/2026, 7:44:14 PM
1class Solution:
2    def minDistance(self, word1: str, word2: str) -> int:
3        # 法二 dp table：自底向上
4        len1, len2 = len(word1), len(word2)
5        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
6
7        # Initialize with base case
8        for i in range(len1 + 1): dp[i][0] = i
9        for j in range(len2 + 1): dp[0][j] = j
10
11        for i in range(1, len1 + 1):
12            for j in range(1, len2 + 1):
13                if word1[i - 1] == word2[j - 1]:
14                    dp[i][j] = dp[i - 1][j - 1]
15                else:
16                    dp[i][j] = self.min3(
17                        dp[i - 1][j] + 1,
18                        dp[i][j - 1] + 1,
19                        dp[i - 1][j - 1] + 1
20                    )
21        
22        return dp[len1][len2]
23    
24    def min3(self, a, b, c):
25        return min(a, min(b, c))