class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtracking([], result, nums, target, 0)
        return result
        
    def backtracking(self, path, result, options, target, startIndex):
        if sum(path) == target:
            result.append(path[:])
            return
        elif sum(path) > target:
            return
        for index in range(startIndex, len(options)):
            num = options[index]
            path.append(num)
            self.backtracking(path, result, options, target, index)
            path.pop()