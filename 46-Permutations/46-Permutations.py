class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.backtrack([], nums, results)
        return results

    def backtrack(self, path, nums, results):
        if len(path) == len(nums):
            results.append(path[:])
        for num in nums:
            if num not in path:
                path.append(num)
                self.backtrack(path, nums, results)
                path.pop()