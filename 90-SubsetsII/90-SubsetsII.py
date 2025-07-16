# Last updated: 7/16/2025, 1:06:47 AM
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.track = []
        nums.sort()
        self.backtrack(nums, 0)
        return self.result
    
    def backtrack(self, nums, start):
        self.result.append(self.track.copy())
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]: continue
            self.track.append(nums[i])
            self.backtrack(nums, i + 1)
            self.track.pop()