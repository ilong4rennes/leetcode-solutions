# Last updated: 7/30/2025, 7:01:31 AM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.track = []
        self.trackSum = 0
        self.backtrack(candidates, target, 0)
        return self.result
    
    def backtrack(self, candidates, target, start):
        if self.trackSum == target:
            self.result.append(self.track.copy())
            return
        if self.trackSum > target:
            return
        for i in range(start, len(candidates)):
            self.track.append(candidates[i])
            self.trackSum += candidates[i]
            self.backtrack(candidates, target, i)
            self.trackSum -= candidates[i]
            self.track.pop()