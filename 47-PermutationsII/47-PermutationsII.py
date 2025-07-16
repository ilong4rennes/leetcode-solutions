# Last updated: 7/16/2025, 1:33:37 AM
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.track = []
        self.used = [False] * len(nums)
        nums.sort()
        self.backtrack(nums)
        return self.result
    
    def backtrack(self, nums):
        if len(self.track) == len(nums):
            self.result.append(self.track.copy())
        for i in range(0, len(nums)):
            if self.used[i]: continue
            if i > 0 and nums[i] == nums[i - 1] and not self.used[i - 1]: continue

            self.track.append(nums[i])
            self.used[i] = True
            self.backtrack(nums)
            self.used[i] = False
            self.track.pop()