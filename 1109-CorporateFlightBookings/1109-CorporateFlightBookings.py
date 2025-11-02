# Last updated: 11/2/2025, 5:08:36 PM
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
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        nums = [0] * n
        diff = Diff(nums)
        for booking in bookings:
            first, last, seats = booking
            diff.increment(first - 1, last - 1, seats)
        return diff.result()        