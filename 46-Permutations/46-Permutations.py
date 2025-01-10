class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        self.backtrack([], nums)
        return self.results

    def backtrack(self, path, nums):
        if len(path) == len(nums):
            self.results.append(path[:])
        for num in nums:
            if num not in path:
                path.append(num)
                self.backtrack(path, nums)
                path.pop()