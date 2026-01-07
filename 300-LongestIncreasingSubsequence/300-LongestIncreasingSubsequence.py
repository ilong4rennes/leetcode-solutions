# Last updated: 1/7/2026, 11:54:39 PM
1class Solution:
2    def lengthOfLIS(self, nums: List[int]) -> int:
3        dp = [1] * len(nums)
4        for i in range(len(nums)):
5            for j in range(0, i, 1):
6                if nums[j] < nums[i]:
7                    dp[i] = max(dp[i], dp[j] + 1)
8        result = max(dp)
9        return result