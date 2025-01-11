class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.visited = [False] * len(nums)
        self.backtrack([], nums)
        return self.result
        
    def backtrack(self, path, nums):
        if len(path) == len(nums) and path[:] not in self.result:
            self.result.append(path[:])
        for i in range(len(nums)):
            if not self.visited[i]:
                self.visited[i] = True
                path.append(nums[i])
                self.backtrack(path, nums)
                path.pop()
                self.visited[i] = False
