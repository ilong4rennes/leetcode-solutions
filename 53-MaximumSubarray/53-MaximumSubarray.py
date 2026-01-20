# Last updated: 1/19/2026, 7:10:02 PM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        dp = [0] * len(nums)
4        dp[0] = nums[0]
5        for i in range(1, len(nums)):
6            dp[i] = max(dp[i - 1] + nums[i], nums[i])
7        return max(dp)