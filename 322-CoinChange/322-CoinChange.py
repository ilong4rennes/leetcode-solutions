# Last updated: 12/29/2025, 2:54:41 AM
1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        self.memo = [-174] * (amount + 1)
4        return self.dp(amount, coins)
5    
6    def dp(self, amount, coins):
7        # dp(amount) 表示凑出amount所需的最少硬币数
8        if amount == 0: return 0
9        if amount < 0: return -1
10        if self.memo[amount] != -174: return self.memo[amount]
11        result = float('inf')
12        for coin in coins:
13            subproblem = self.dp(amount - coin, coins)
14            if subproblem == -1: continue
15            result = min(result, subproblem + 1)
16        self.memo[amount] = result if result != float('inf') else -1
17        return self.memo[amount]