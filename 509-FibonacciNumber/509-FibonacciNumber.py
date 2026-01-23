# Last updated: 1/23/2026, 5:23:05 AM
1class Solution:
2    def fib(self, n: int) -> int:
3        self.memo = [-174] * (n + 1)
4        return self.dp(n)
5    
6    def dp(self, n):
7        if n == 0 or n == 1:
8            return n
9        if self.memo[n] != -174:
10            return self.memo[n]
11        self.memo[n] = self.dp(n - 1) + self.dp(n - 2)
12        return self.memo[n]