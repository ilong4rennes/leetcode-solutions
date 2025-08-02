# Last updated: 8/2/2025, 8:24:40 AM
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [i for i in range(1, 10)]
        self.result = []
        self.track = []
        start = 0
        self.backtrack(start, candidates, n, k)
        return self.result
    
    def backtrack(self, start, candidates, target, k):
        if sum(self.track) == target and len(self.track) == k:
            self.result.append(self.track.copy())
            return
        if sum(self.track) > target:
            return
        for i in range(start, len(candidates)):
            self.track.append(candidates[i])
            self.backtrack(i + 1, candidates, target, k)
            self.track.pop()