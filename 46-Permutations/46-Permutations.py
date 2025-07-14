# Last updated: 7/14/2025, 3:31:04 AM
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        track = []
        used = [False] * len(nums)
        self.backtrack(nums, track, used)
        return self.result
    
    def backtrack(self, nums, track, used):
        if len(track) == len(nums):
            self.result.append(track.copy())
            return
        for i in range(len(nums)):
            if used[i] == True:
                continue
            used[i] = True
            track.append(nums[i])
            self.backtrack(nums, track, used)
            track.pop()
            used[i] = False