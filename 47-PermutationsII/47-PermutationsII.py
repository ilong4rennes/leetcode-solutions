# Last updated: 7/30/2025, 4:31:08 AM
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
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and self.used[i - 1] == False:
                continue
            if self.used[i] == False:
                self.track.append(nums[i])
                self.used[i] = True
                self.backtrack(nums)
                self.used[i] = False
                self.track.pop()