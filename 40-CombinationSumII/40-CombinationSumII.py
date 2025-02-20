class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        used = [0] * len(candidates)
        self.backtracking(sorted(candidates), target, 0, used, [], result)
        return result
        
    def backtracking(self, options, target, startIndex, used, path, result):
        if sum(path) == target:
            result.append(path[:])
            return
        elif sum(path) > target:
            return
        for index in range(startIndex, len(options)):
            if index > startIndex and options[index] == options[index - 1] and used[index - 1] == False:
                continue
            path.append(options[index])
            used[index] = True
            self.backtracking(options, target, index + 1, used, path, result)
            used[index] = False
            path.pop()