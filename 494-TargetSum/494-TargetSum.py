# Last updated: 1/23/2026, 4:52:31 AM
1class Solution:
2    def findTargetSumWays(self, nums: List[int], target: int) -> int:
3        total_sum = sum(nums)
4        if abs(target) > total_sum:
5            return 0
6        if (total_sum + target) % 2 != 0:
7            return 0
8        
9        P = (total_sum + target) // 2
10        n = len(nums)
11
12        dp = [[0] * (P + 1) for _ in range(n + 1)]
13        dp[0][0] = 1  # base case
14
15        for i in range(1, n + 1):
16            for j in range(0, P + 1):
17                if j - nums[i - 1] < 0:
18                    dp[i][j] = dp[i - 1][j]
19                else:
20                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
21
22        return dp[n][P]