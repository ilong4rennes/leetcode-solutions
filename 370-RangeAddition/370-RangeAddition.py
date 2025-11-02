# Last updated: 11/2/2025, 4:12:00 PM
class Diff:
    def __init__(self, nums):
        self.diff = [0] * len(nums)
        self.diff[0] = nums[0]
        for i in range(1, len(nums)):
            self.diff[i] = nums[i] - nums[i - 1]
    
    def increment(self, startId, endId, inc):
        self.diff[startId] += inc
        if endId + 1 < len(self.diff):
            self.diff[endId + 1] -= inc
    
    def result(self):
        result = [0] * len(self.diff)
        result[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            result[i] = result[i - 1] + self.diff[i]
        return result
 
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        nums = [0] * length
        diff = Diff(nums)
        for update in updates:
            startId, endId, inc = update
            diff.increment(startId, endId, inc)
        return diff.result()