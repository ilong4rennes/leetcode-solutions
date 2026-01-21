# Last updated: 1/21/2026, 4:02:10 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        self.memo = [-174] * (len(nums) + 1)
4        return self.dp(nums, 0)
5    
6    def dp(self, nums, index):
7        if index >= len(nums): return 0
8        if self.memo[index] != -174: return self.memo[index]
9        self.memo[index] = max(nums[index] + self.dp(nums, index + 2),
10                               self.dp(nums, index + 1))
11        return self.memo[index]