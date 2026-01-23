# Last updated: 1/23/2026, 4:23:49 AM
1class Solution:
2    def minInsertions(self, s: str) -> int:
3        n = len(s)
4        dp = [[0] * n for _ in range(n)]
5        for i in range(n - 1, -1, -1):
6            for j in range(i + 1, n):
7                if s[i] == s[j]:
8                    dp[i][j] = dp[i + 1][j - 1]
9                else:
10                    dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + 1
11        return dp[0][n - 1]