# Last updated: 1/10/2026, 2:30:41 AM
1class Solution:
2    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
3        dp = [[0] * (n + 1) for _ in range(m + 1)]
4        for s in strs:
5            zeros = s.count('0')
6            ones = s.count('1')
7            for i in range(m, zeros - 1, -1):
8                for j in range(n, ones - 1, -1):
9                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
10        return dp[m][n]