class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        options = [i for i in range(1, 10)]
        result = []
        self.backtracking([], result, options, k, n, 0)
        return result
    
    def backtracking(self, path, result, options, k, target, startIndex):
        if sum(path) == target and len(path) == k:
            result.append(path[:])
            return
        elif sum(path) > target:
            return
        for i in range(startIndex, len(options)):
            path.append(options[i])
            if len(path) <= k:
                self.backtracking(path, result, options, k, target, i + 1)
            path.pop()