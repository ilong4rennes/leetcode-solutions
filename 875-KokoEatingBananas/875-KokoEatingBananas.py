# Last updated: 4/27/2025, 9:00:47 PM
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if self.canFinishOnTime(piles, h, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def canFinishOnTime(self, piles, maxHour, speed):
        totalHours = 0
        for pile in piles:
            totalHours += math.ceil(pile / speed)
        return totalHours <= maxHour