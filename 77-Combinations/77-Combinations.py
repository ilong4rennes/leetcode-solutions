# Last updated: 7/15/2025, 2:30:46 AM
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []
        self.track = []
        nums = [i for i in range(1, n + 1)]
        self.backtrack(nums, k, 1)
        return self.result
    
    def backtrack(self, nums, k, start):
        if len(self.track) == k:
            self.result.append(self.track.copy())
            return
        for i in range(start, len(nums) + 1):
            self.track.append(i)
            self.backtrack(nums, k, i + 1)
            self.track.pop()