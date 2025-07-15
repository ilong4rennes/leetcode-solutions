# Last updated: 7/15/2025, 12:01:24 AM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.track = []
        self.backtrack(nums, 0)
        return self.result
    
    def backtrack(self, nums, start):
        self.result.append(self.track.copy())
        for i in range(start, len(nums)):
            self.track.append(nums[i])
            self.backtrack(nums, i + 1)
            self.track.pop()