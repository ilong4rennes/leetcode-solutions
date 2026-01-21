# Last updated: 1/21/2026, 4:26:32 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        if len(nums) == 1: return nums[0]
4        n = len(nums)
5        memo1, memo2 = {}, {}
6        return max(self.dp(nums, 0, n - 2, memo1),
7                   self.dp(nums, 1, n - 1, memo2))
8    
9    def dp(self, nums, start, end, memo):
10        n = len(nums)
11        if start > end: return 0
12        if start in memo: return memo[start]
13        memo[start] = max(nums[start] + self.dp(nums, start + 2, end, memo),
14                      self.dp(nums, start + 1, end, memo))
15        return memo[start]