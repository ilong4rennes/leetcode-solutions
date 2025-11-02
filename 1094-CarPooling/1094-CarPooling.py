# Last updated: 11/2/2025, 5:32:18 PM
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
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        nums = [0] * 1001
        diff = Diff(nums)
        for trip in trips:
            numPas, _from, _to = trip
            diff.increment(_from, _to - 1, numPas)
        result = diff.result()
        for passengers in result:
            if passengers > capacity:
                return False
        return True