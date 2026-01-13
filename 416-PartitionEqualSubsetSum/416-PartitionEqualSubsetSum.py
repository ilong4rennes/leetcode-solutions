# Last updated: 1/13/2026, 12:21:37 PM
1class Solution:
2    def canPartition(self, nums: List[int]) -> bool:
3        total = sum(nums)
4        if total % 2 != 0: return False
5        target = total // 2
6        dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]
7
8        # Base case
9        for i in range(len(nums) + 1):
10            dp[i][0] = True
11
12        for i in range(1, len(nums) + 1):
13            for w in range(1, target + 1):
14                if w < nums[i - 1]:
15                    dp[i][w] = dp[i - 1][w]
16                else:
17                    dp[i][w] = (dp[i - 1][w] or
18                                dp[i - 1][w - nums[i - 1]]
19                    )
20        return dp[len(nums)][target]
21
22