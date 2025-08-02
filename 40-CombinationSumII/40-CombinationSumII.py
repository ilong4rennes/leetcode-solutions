# Last updated: 8/2/2025, 7:45:17 AM
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.track = []
        self.used = [False] * len(candidates)
        candidates.sort()
        start = 0
        self.backtrack(start, candidates, target)
        return self.result
    
    def backtrack(self, start, candidates, target):
        if sum(self.track) == target:
            self.result.append(self.track.copy())
            return
        if sum(self.track) > target:
            return 
        for i in range(start, len(candidates)):
            if i > 0 and candidates[i] == candidates[i - 1] and self.used[i - 1] == False:
                continue
            self.track.append(candidates[i])
            self.used[i] = True
            self.backtrack(i + 1, candidates, target)
            self.used[i] = False
            self.track.pop()