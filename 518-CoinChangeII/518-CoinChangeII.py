# Last updated: 1/15/2026, 6:09:02 PM
1class Solution:
2    def change(self, amount: int, coins: List[int]) -> int:
3        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
4        for i in range(len(coins) + 1):
5            dp[i][0] = 1
6        
7        for i in range(1, len(coins) + 1):
8            for w in range(1, amount + 1):
9                if coins[i - 1] > w:
10                    dp[i][w] = dp[i - 1][w]
11                else:
12                    dp[i][w] = (dp[i - 1][w] + 
13                                dp[i][w - coins[i - 1]])
14        
15        return dp[len(coins)][amount]