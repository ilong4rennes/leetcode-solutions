# Last updated: 1/22/2026, 7:54:30 PM
1class Solution:
2    def longestPalindromeSubseq(self, s: str) -> int:
3        n = len(s)
4        dp = [[0] * n for _ in range(n)]
5
6        # Initialize with B.C.
7        for i in range(n):
8            dp[i][i] = 1
9        
10        # Transition
11        for i in range(n - 1, -1, -1):
12            for j in range(i + 1, n):
13                if s[i] == s[j]:
14                    dp[i][j] = dp[i + 1][j - 1] + 2
15                else:
16                    dp[i][j] = max(dp[i][j - 1], 
17                                   dp[i + 1][j])
18        
19        return dp[0][n - 1]