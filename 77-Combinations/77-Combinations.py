class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        options = [i for i in range(1, n + 1)]
        result = []
        self.backtrack([], options, result, n, k)
        return result
        
    def backtrack(self, path, options, result, n, k):
        if len(path) == k:
            result.append(path[:])
            return
        for id in range(len(options)):
            path.append(options[id])
            self.backtrack(path, options[id + 1:], result, n - 1, k)
            path.pop()